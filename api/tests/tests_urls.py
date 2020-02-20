from django.test import TestCase, Client

# Create your tests here.
from django.urls import resolve, reverse
from api.views import UserViewSet, TaskViewSet


def resolve_by_name(name, **kwargs):
    url = reverse(name, kwargs=kwargs)
    return resolve(url)

class UsersUrlsTestCase(TestCase):

    def test_resolves_list_url(self):
        resolver = resolve_by_name('users-list')

        self.assertEqual(resolver.func.cls, UserViewSet)

    def test_resolves_retrieve_url(self):
        resolver = resolve_by_name('users-detail', pk=1)

        self.assertEqual(resolver.func.cls, UserViewSet)

    def test_resolves_url_to_list_action(self):
        resolver = resolve_by_name('users-list')

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('list', resolver.func.actions['get'])
        self.assertEqual('create', resolver.func.actions['post'])

    def test_resolves_url_to_retrieve_action(self):
        resolver = resolve_by_name('users-detail', pk=1)

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('retrieve', resolver.func.actions['get'])
        self.assertEqual('update', resolver.func.actions['put'])
        self.assertEqual('destroy', resolver.func.actions['delete'])


class TaskssUrlsTestCase(TestCase):

    def test_resolves_list_url(self):
        resolver = resolve_by_name('tasks-list')

        self.assertEqual(resolver.func.cls, TaskViewSet)

    def test_resolves_retrieve_url(self):
        resolver = resolve_by_name('tasks-detail', pk=1)

        self.assertEqual(resolver.func.cls, TaskViewSet)

    def test_resolves_url_to_list_action(self):
        resolver = resolve_by_name('tasks-list')

        self.assertIn('get', resolver.func.actions)
        self.assertIn('post', resolver.func.actions)
        self.assertEqual('list', resolver.func.actions['get'])
        self.assertEqual('create', resolver.func.actions['post'])

    def test_resolves_url_to_retrieve_action(self):
        resolver = resolve_by_name('tasks-detail', pk=1)

        self.assertIn('get', resolver.func.actions)
        self.assertIn('put', resolver.func.actions)
        self.assertIn('delete', resolver.func.actions)
        self.assertEqual('retrieve', resolver.func.actions['get'])
        self.assertEqual('update', resolver.func.actions['put'])
        self.assertEqual('destroy', resolver.func.actions['delete'])

    def test_resolves_url_to_users_tasks_action(self):
        resolver = resolve_by_name('tasks-user-tasks', id_user=1)

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('user_tasks', resolver.func.actions['get'])


    def test_resolves_url_to_tasks_states_action(self):
        resolver = resolve_by_name('tasks-states')

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('states', resolver.func.actions['get'])
