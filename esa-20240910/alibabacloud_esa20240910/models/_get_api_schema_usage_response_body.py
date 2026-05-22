# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetApiSchemaUsageResponseBody(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_usage: int = None,
        request_id: str = None,
        usages: List[main_models.GetApiSchemaUsageResponseBodyUsages] = None,
    ):
        # The plan ID.
        self.instance_id = instance_id
        # The number of files uploaded for schema verification in the plan instance of the website.
        self.instance_usage = instance_usage
        # Id of the request
        self.request_id = request_id
        # Usage details for websites.
        self.usages = usages

    def validate(self):
        if self.usages:
            for v1 in self.usages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_usage is not None:
            result['InstanceUsage'] = self.instance_usage

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Usages'] = []
        if self.usages is not None:
            for k1 in self.usages:
                result['Usages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceUsage') is not None:
            self.instance_usage = m.get('InstanceUsage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.usages = []
        if m.get('Usages') is not None:
            for k1 in m.get('Usages'):
                temp_model = main_models.GetApiSchemaUsageResponseBodyUsages()
                self.usages.append(temp_model.from_map(k1))

        return self

class GetApiSchemaUsageResponseBodyUsages(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        usage: int = None,
    ):
        # The website ID.
        self.id = id
        # The website name.
        self.name = name
        # The number of files uploaded for the website.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

