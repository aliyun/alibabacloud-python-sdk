# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateTrafficMirrorFilterRulesResponseBody(DaraModel):
    def __init__(
        self,
        egress_rules: List[main_models.CreateTrafficMirrorFilterRulesResponseBodyEgressRules] = None,
        ingress_rules: List[main_models.CreateTrafficMirrorFilterRulesResponseBodyIngressRules] = None,
        request_id: str = None,
    ):
        # The list of outbound rules.
        self.egress_rules = egress_rules
        # The list of inbound rules.
        self.ingress_rules = ingress_rules
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.egress_rules:
            for v1 in self.egress_rules:
                 if v1:
                    v1.validate()
        if self.ingress_rules:
            for v1 in self.ingress_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EgressRules'] = []
        if self.egress_rules is not None:
            for k1 in self.egress_rules:
                result['EgressRules'].append(k1.to_map() if k1 else None)

        result['IngressRules'] = []
        if self.ingress_rules is not None:
            for k1 in self.ingress_rules:
                result['IngressRules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.egress_rules = []
        if m.get('EgressRules') is not None:
            for k1 in m.get('EgressRules'):
                temp_model = main_models.CreateTrafficMirrorFilterRulesResponseBodyEgressRules()
                self.egress_rules.append(temp_model.from_map(k1))

        self.ingress_rules = []
        if m.get('IngressRules') is not None:
            for k1 in m.get('IngressRules'):
                temp_model = main_models.CreateTrafficMirrorFilterRulesResponseBodyIngressRules()
                self.ingress_rules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateTrafficMirrorFilterRulesResponseBodyIngressRules(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the inbound rule.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class CreateTrafficMirrorFilterRulesResponseBodyEgressRules(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the outbound rule.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

