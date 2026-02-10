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
        # An array consisting of the filter conditions that are supported by the image repository.
        self.criteria_list = criteria_list
        # The ID of the request, which is used to locate and troubleshoot issues.
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
        # The name of the search condition. Valid values:
        # 
        # *   **instanceId**: the ID of the image instance.
        # *   **repoName**: the name of the image repository.
        # *   **repoId**: the ID of the image repository.
        # *   **repoNamespace**: the namespace of the image repository.
        # *   **regionId**: the region in which the image resides.
        # *   **vulStatus**: indicates whether vulnerabilities exist.
        # *   **alarmStatus**: indicates whether security alerts exist.
        # *   **hcStatus**: indicates whether baseline risks exist.
        # *   **riskStatus**: indicates whether risks exist.
        # *   **registryType**: the type of the image repository.
        # *   **ImageId**: the image ID.
        # *   **tag**: the image tag.
        self.name = name
        # The type of the search condition. Valid values:
        # 
        # *   **input**: The search condition needs to be specified.
        # *   **select**: The search condition is an option that can be selected from the drop-down list.
        self.type = type
        # The values of the search condition. This parameter is returned only if the value of **Type** is set to **select**.
        # 
        # > If the value of **Type** is set to **input**, the return value of this parameter is empty.
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

