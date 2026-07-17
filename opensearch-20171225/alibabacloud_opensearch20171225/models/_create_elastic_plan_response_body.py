# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class CreateElasticPlanResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.CreateElasticPlanResponseBodyResult = None,
    ):
        self.code = code
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.CreateElasticPlanResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class CreateElasticPlanResponseBodyResult(DaraModel):
    def __init__(
        self,
        app_group_id: str = None,
        created: int = None,
        custom_dates: List[str] = None,
        description: str = None,
        elastic_lcu: int = None,
        enabled: bool = None,
        end_hour: int = None,
        id: int = None,
        name: str = None,
        schedule_type: str = None,
        start_hour: int = None,
        updated: int = None,
    ):
        self.app_group_id = app_group_id
        self.created = created
        self.custom_dates = custom_dates
        self.description = description
        self.elastic_lcu = elastic_lcu
        self.enabled = enabled
        self.end_hour = end_hour
        self.id = id
        self.name = name
        self.schedule_type = schedule_type
        self.start_hour = start_hour
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_group_id is not None:
            result['appGroupId'] = self.app_group_id

        if self.created is not None:
            result['created'] = self.created

        if self.custom_dates is not None:
            result['customDates'] = self.custom_dates

        if self.description is not None:
            result['description'] = self.description

        if self.elastic_lcu is not None:
            result['elasticLcu'] = self.elastic_lcu

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.end_hour is not None:
            result['endHour'] = self.end_hour

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.schedule_type is not None:
            result['scheduleType'] = self.schedule_type

        if self.start_hour is not None:
            result['startHour'] = self.start_hour

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appGroupId') is not None:
            self.app_group_id = m.get('appGroupId')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('customDates') is not None:
            self.custom_dates = m.get('customDates')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('elasticLcu') is not None:
            self.elastic_lcu = m.get('elasticLcu')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('endHour') is not None:
            self.end_hour = m.get('endHour')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('scheduleType') is not None:
            self.schedule_type = m.get('scheduleType')

        if m.get('startHour') is not None:
            self.start_hour = m.get('startHour')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

