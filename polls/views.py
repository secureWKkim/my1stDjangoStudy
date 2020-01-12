from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last 5 published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ',<br>'.join([q.question_text   for q in latest_question_list])
    content = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', content)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    content = {'question' : question}
    return render(request, 'polls/detail.html', content)


def retults(request, question_id):
    question = get_object_or_404(Choice, pk=question_id)
    content = {'question':question}
    return render(request, 'polls/result.html', content)
    # return HttpResponse("질문의 답은 {} 입니다.".format(question_id))


def vote(request, question_id):
    # 기본키 목록을 호출
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Pk와 연결된 종속키 내용을 호출
        selected_choice = question.choice_set.get(
            pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 투표용 Form을 ReRoaded
        content = {
            'question': question,
            'error_message':'아직 선택한 내용이 없습니다'
        }
        return render(request, 'polls/detail.html', content)
    else:
        # try, except, else 구문을 잘 익히자 !!
        # try를 정상 통과된 경우에만 실행 할 내용
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))