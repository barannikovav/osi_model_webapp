'''layers Django app views configuration'''
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, F
from .models import OSILayer, Question

def index(request):
    '''Page with layers list'''
    layers = OSILayer.objects.all().order_by('number')
    return render(request, "layers/index.html", {'layers': layers})

def detail(request, layer_id):
    '''Page with layer's detailed description'''
    layer = get_object_or_404(OSILayer, number=layer_id)
    return render(request, "layers/layer.html", {'layer': layer})

def test(request, layer_id):
    '''Page with test about layer's description'''
    layer = get_object_or_404(OSILayer, number=layer_id)
    questions = Question.objects.filter(layer__number=layer_id)
    if request.method == 'POST':
        score = 0
        total = questions.count()
        results = []

        for question in questions:
            selected_answer = request.POST.get(f'question_{question.id}')
            correct_answers = question.answer.split('|')
            correct_answers_lower = [a.lower() for a in correct_answers]
            if selected_answer:
                is_correct = selected_answer.strip().lower() in correct_answers_lower
                if is_correct:
                    score += 1
                    question.num_of_correct = F("num_of_correct") + 1
                question.num_of_answers = F("num_of_answers") + 1
                question.save()

                results.append({
                    'selected_answer': selected_answer,
                    'correct_answer': ', '.join(correct_answers),
                    'question': question,
                    'is_correct': is_correct,
                    'explanation': question.explanation
                })
        n_ans = (int(list(questions.aggregate(Sum('num_of_answers')).values())[0]/total)
                 if total > 0 else 0)
        avr = list(questions.aggregate(Sum('num_of_correct')).values())[0]/n_ans if n_ans > 0 else 0
        avr = round(avr, 2)


        return render(request, 'layers/layer_test_result.html', {
            'layer': layer,
            'score': score,
            'total': total,
            'results': results,
            'percentage': int((score / total) * 100) if total > 0 else 0,
            'average' : avr,
            'average_percentage': int((avr/total) * 100) if n_ans > 0 else 0,
            'n_ans' : n_ans
        })
    return render(request, "layers/layer_test.html", {'layer': layer, 'questions': questions})
