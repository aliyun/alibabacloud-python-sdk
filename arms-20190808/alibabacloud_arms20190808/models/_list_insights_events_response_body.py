# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListInsightsEventsResponseBody(DaraModel):
    def __init__(
        self,
        insights_events: List[main_models.ListInsightsEventsResponseBodyInsightsEvents] = None,
        request_id: str = None,
    ):
        # The details of the event.
        self.insights_events = insights_events
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.insights_events:
            for v1 in self.insights_events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InsightsEvents'] = []
        if self.insights_events is not None:
            for k1 in self.insights_events:
                result['InsightsEvents'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.insights_events = []
        if m.get('InsightsEvents') is not None:
            for k1 in m.get('InsightsEvents'):
                temp_model = main_models.ListInsightsEventsResponseBodyInsightsEvents()
                self.insights_events.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInsightsEventsResponseBodyInsightsEvents(DaraModel):
    def __init__(
        self,
        date: int = None,
        desc: str = None,
        level: str = None,
        pid: str = None,
        problem_id: str = None,
        title: str = None,
        type: str = None,
    ):
        # The time when the event occurred. The value is a timestamp.
        self.date = date
        # The description of the alert event.
        self.desc = desc
        # The severity of the event.
        self.level = level
        # The ID of the application associated with the event.
        self.pid = pid
        # The problem identifier.
        self.problem_id = problem_id
        # The title of the event.
        self.title = title
        # The type of the event.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.level is not None:
            result['Level'] = self.level

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.problem_id is not None:
            result['ProblemId'] = self.problem_id

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('ProblemId') is not None:
            self.problem_id = m.get('ProblemId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

