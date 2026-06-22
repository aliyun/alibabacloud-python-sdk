# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageRepoCriteriaResponseBody(DaraModel):
    def __init__(
        self,
        criteria_list: List[main_models.DescribeImageRepoCriteriaResponseBodyCriteriaList] = None,
        request_id: str = None,
    ):
        # The list of supported search criteria for image repositories.
        self.criteria_list = criteria_list
        # The request ID. Alibaba Cloud generates a unique identifier for each API request. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.criteria_list:
            for v1 in self.criteria_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CriteriaList'] = []
        if self.criteria_list is not None:
            for k1 in self.criteria_list:
                result['CriteriaList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.criteria_list = []
        if m.get('CriteriaList') is not None:
            for k1 in m.get('CriteriaList'):
                temp_model = main_models.DescribeImageRepoCriteriaResponseBodyCriteriaList()
                self.criteria_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageRepoCriteriaResponseBodyCriteriaList(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        values: str = None,
    ):
        # The name of the search criterion. Valid values:
        # 
        # - **instanceId**: image instance ID.
        # - **repoName**: repository name.
        # - **repoId**: repository ID.
        # - **repoNamespace**: repository namespace.
        # - **regionId**: image region.
        # - **vulStatus**: whether vulnerabilities exist.
        # - **alarmStatus**: whether security alerts exist.
        # - **hcStatus**: whether baseline risks exist.
        # - **riskStatus**: whether risks exist.
        # - **registryType**: repository type.
        # - **imageId**: image ID.
        # - **tag**: image tag.
        self.name = name
        # The type of the search criterion. Valid values:
        # 
        # - **input**: requires manual input of the search field.
        # - **select**: requires selecting a subtype from a drop-down list.
        self.type = type
        # The available options when **Type** (the type of the search criterion) is **select** (selection type).
        # > When **Type** (the type of the search criterion) is **input** (input type), this parameter returns an empty value.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

