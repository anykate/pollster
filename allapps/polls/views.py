from django.shortcuts import render, get_object_or_404, reverse
from .models import Question, Choice
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')
    return render(request, 'polls/index.html', {'questions': latest_question_list})


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
