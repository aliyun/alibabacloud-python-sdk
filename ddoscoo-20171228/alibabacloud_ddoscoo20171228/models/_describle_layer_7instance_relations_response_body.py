# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribleLayer7InstanceRelationsResponseBody(DaraModel):
    def __init__(
        self,
        layer_7instance_relations: List[main_models.DescribleLayer7InstanceRelationsResponseBodyLayer7InstanceRelations] = None,
        request_id: str = None,
    ):
        self.layer_7instance_relations = layer_7instance_relations
        self.request_id = request_id

    def validate(self):
        if self.layer_7instance_relations:
            for v1 in self.layer_7instance_relations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Layer7InstanceRelations'] = []
        if self.layer_7instance_relations is not None:
            for k1 in self.layer_7instance_relations:
                result['Layer7InstanceRelations'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layer_7instance_relations = []
        if m.get('Layer7InstanceRelations') is not None:
            for k1 in m.get('Layer7InstanceRelations'):
                temp_model = main_models.DescribleLayer7InstanceRelationsResponseBodyLayer7InstanceRelations()
                self.layer_7instance_relations.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribleLayer7InstanceRelationsResponseBodyLayer7InstanceRelations(DaraModel):
    def __init__(
        self,
        domain: str = None,
        instance_details: List[main_models.DescribleLayer7InstanceRelationsResponseBodyLayer7InstanceRelationsInstanceDetails] = None,
    ):
        self.domain = domain
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
                temp_model = main_models.DescribleLayer7InstanceRelationsResponseBodyLayer7InstanceRelationsInstanceDetails()
                self.instance_details.append(temp_model.from_map(k1))

        return self

class DescribleLayer7InstanceRelationsResponseBodyLayer7InstanceRelationsInstanceDetails(DaraModel):
    def __init__(
        self,
        eip_list: List[str] = None,
        function_version: str = None,
        instance_id: str = None,
        ip_mode: str = None,
        ip_version: str = None,
    ):
        self.eip_list = eip_list
        self.function_version = function_version
        self.instance_id = instance_id
        self.ip_mode = ip_mode
        self.ip_version = ip_version

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

        if self.ip_mode is not None:
            result['IpMode'] = self.ip_mode

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipList') is not None:
            self.eip_list = m.get('EipList')

        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IpMode') is not None:
            self.ip_mode = m.get('IpMode')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        return self

