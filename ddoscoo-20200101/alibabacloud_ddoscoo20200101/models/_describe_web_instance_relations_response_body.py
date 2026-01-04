# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeWebInstanceRelationsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        web_instance_relations: List[main_models.DescribeWebInstanceRelationsResponseBodyWebInstanceRelations] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the instances to which a website service is added.
        self.web_instance_relations = web_instance_relations

    def validate(self):
        if self.web_instance_relations:
            for v1 in self.web_instance_relations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['WebInstanceRelations'] = []
        if self.web_instance_relations is not None:
            for k1 in self.web_instance_relations:
                result['WebInstanceRelations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.web_instance_relations = []
        if m.get('WebInstanceRelations') is not None:
            for k1 in m.get('WebInstanceRelations'):
                temp_model = main_models.DescribeWebInstanceRelationsResponseBodyWebInstanceRelations()
                self.web_instance_relations.append(temp_model.from_map(k1))

        return self

class DescribeWebInstanceRelationsResponseBodyWebInstanceRelations(DaraModel):
    def __init__(
        self,
        domain: str = None,
        instance_details: List[main_models.DescribeWebInstanceRelationsResponseBodyWebInstanceRelationsInstanceDetails] = None,
    ):
        # The domain name of the website.
        self.domain = domain
        # The information about the instance to which a website service is added.
        self.instance_details = instance_details

    def validate(self):
        if self.instance_details:
            for v1 in self.instance_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        result['InstanceDetails'] = []
        if self.instance_details is not None:
            for k1 in self.instance_details:
                result['InstanceDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        self.instance_details = []
        if m.get('InstanceDetails') is not None:
            for k1 in m.get('InstanceDetails'):
                temp_model = main_models.DescribeWebInstanceRelationsResponseBodyWebInstanceRelationsInstanceDetails()
                self.instance_details.append(temp_model.from_map(k1))

        return self

class DescribeWebInstanceRelationsResponseBodyWebInstanceRelationsInstanceDetails(DaraModel):
    def __init__(
        self,
        eip_list: List[str] = None,
        function_version: str = None,
        instance_id: str = None,
    ):
        # The IP addresses of the instance.
        self.eip_list = eip_list
        # The function plan of the instance. Valid values:
        # 
        # *   **default**: Standard function plan
        # *   **enhance**: Enhanced function plan
        self.function_version = function_version
        # The ID of the instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_list is not None:
            result['EipList'] = self.eip_list

        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipList') is not None:
            self.eip_list = m.get('EipList')

        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

