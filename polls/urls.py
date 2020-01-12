from django.urls import path
from . import views


app_name = 'polls'  # namespace
"""
path(route, view, kwargs, name) 형태의 함수.
route = 주소  view = route 주소로 접근했을 때 호출할 뷰   kwargs = 뷰에 전달할 값들
name = route 의 이름 의미. 이 이름을 갖고 원하는 곳에서 주소를 호출해 출력하거나 사용할 수 있음.
polls 폴더에 있는 urls.py 는 앱의 라우팅만 담당. 프로젝트의 메인 urls.py 파일에서 연결을 해줘야 정상 동작함.
"""
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
