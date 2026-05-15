# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class MeetingFlashMinutesResponseBody(DaraModel):
    def __init__(
        self,
        basic_info: main_models.MeetingFlashMinutesResponseBodyBasicInfo = None,
        flash_minutes_url: str = None,
        full_summary: str = None,
        request_id: str = None,
        todos: main_models.MeetingFlashMinutesResponseBodyTodos = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.basic_info = basic_info
        self.flash_minutes_url = flash_minutes_url
        self.full_summary = full_summary
        self.request_id = request_id
        self.todos = todos
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.basic_info:
            self.basic_info.validate()
        if self.todos:
            self.todos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_info is not None:
            result['basicInfo'] = self.basic_info.to_map()

        if self.flash_minutes_url is not None:
            result['flashMinutesUrl'] = self.flash_minutes_url

        if self.full_summary is not None:
            result['fullSummary'] = self.full_summary

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.todos is not None:
            result['todos'] = self.todos.to_map()

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basicInfo') is not None:
            temp_model = main_models.MeetingFlashMinutesResponseBodyBasicInfo()
            self.basic_info = temp_model.from_map(m.get('basicInfo'))

        if m.get('flashMinutesUrl') is not None:
            self.flash_minutes_url = m.get('flashMinutesUrl')

        if m.get('fullSummary') is not None:
            self.full_summary = m.get('fullSummary')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('todos') is not None:
            temp_model = main_models.MeetingFlashMinutesResponseBodyTodos()
            self.todos = temp_model.from_map(m.get('todos'))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class MeetingFlashMinutesResponseBodyTodos(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        dingtalk_todo_list: List[main_models.MeetingFlashMinutesResponseBodyTodosDingtalkTodoList] = None,
    ):
        self.actions = actions
        self.dingtalk_todo_list = dingtalk_todo_list

    def validate(self):
        if self.dingtalk_todo_list:
            for v1 in self.dingtalk_todo_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        result['dingtalkTodoList'] = []
        if self.dingtalk_todo_list is not None:
            for k1 in self.dingtalk_todo_list:
                result['dingtalkTodoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        self.dingtalk_todo_list = []
        if m.get('dingtalkTodoList') is not None:
            for k1 in m.get('dingtalkTodoList'):
                temp_model = main_models.MeetingFlashMinutesResponseBodyTodosDingtalkTodoList()
                self.dingtalk_todo_list.append(temp_model.from_map(k1))

        return self

class MeetingFlashMinutesResponseBodyTodosDingtalkTodoList(DaraModel):
    def __init__(
        self,
        created_time: int = None,
        creator_union_id: str = None,
        deadline: str = None,
        dingtalk_todo_id: str = None,
        executor_list: List[main_models.MeetingFlashMinutesResponseBodyTodosDingtalkTodoListExecutorList] = None,
        is_done: bool = None,
        minutes_todo_id: str = None,
        title: str = None,
    ):
        self.created_time = created_time
        self.creator_union_id = creator_union_id
        self.deadline = deadline
        self.dingtalk_todo_id = dingtalk_todo_id
        self.executor_list = executor_list
        self.is_done = is_done
        self.minutes_todo_id = minutes_todo_id
        self.title = title

    def validate(self):
        if self.executor_list:
            for v1 in self.executor_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.creator_union_id is not None:
            result['creatorUnionId'] = self.creator_union_id

        if self.deadline is not None:
            result['deadline'] = self.deadline

        if self.dingtalk_todo_id is not None:
            result['dingtalkTodoId'] = self.dingtalk_todo_id

        result['executorList'] = []
        if self.executor_list is not None:
            for k1 in self.executor_list:
                result['executorList'].append(k1.to_map() if k1 else None)

        if self.is_done is not None:
            result['isDone'] = self.is_done

        if self.minutes_todo_id is not None:
            result['minutesTodoId'] = self.minutes_todo_id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('creatorUnionId') is not None:
            self.creator_union_id = m.get('creatorUnionId')

        if m.get('deadline') is not None:
            self.deadline = m.get('deadline')

        if m.get('dingtalkTodoId') is not None:
            self.dingtalk_todo_id = m.get('dingtalkTodoId')

        self.executor_list = []
        if m.get('executorList') is not None:
            for k1 in m.get('executorList'):
                temp_model = main_models.MeetingFlashMinutesResponseBodyTodosDingtalkTodoListExecutorList()
                self.executor_list.append(temp_model.from_map(k1))

        if m.get('isDone') is not None:
            self.is_done = m.get('isDone')

        if m.get('minutesTodoId') is not None:
            self.minutes_todo_id = m.get('minutesTodoId')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class MeetingFlashMinutesResponseBodyTodosDingtalkTodoListExecutorList(DaraModel):
    def __init__(
        self,
        avatar: str = None,
        nick: str = None,
        union_id: str = None,
    ):
        self.avatar = avatar
        self.nick = nick
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar is not None:
            result['avatar'] = self.avatar

        if self.nick is not None:
            result['nick'] = self.nick

        if self.union_id is not None:
            result['unionId'] = self.union_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')

        if m.get('nick') is not None:
            self.nick = m.get('nick')

        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')

        return self

class MeetingFlashMinutesResponseBodyBasicInfo(DaraModel):
    def __init__(
        self,
        duration: int = None,
        end_time: int = None,
        start_time: int = None,
        task_creator: str = None,
        title: str = None,
        url: str = None,
    ):
        self.duration = duration
        self.end_time = end_time
        self.start_time = start_time
        self.task_creator = task_creator
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['duration'] = self.duration

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.task_creator is not None:
            result['taskCreator'] = self.task_creator

        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('taskCreator') is not None:
            self.task_creator = m.get('taskCreator')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

