# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class ListNodeInfosForPodResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: List[main_models.ListNodeInfosForPodResponseBodyContent] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The information about the request denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # Response body
        self.content = content
        # The returned message.
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.ListNodeInfosForPodResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListNodeInfosForPodResponseBodyContent(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        hdeni_quota: int = None,
        leni_quota: int = None,
        leni_sip_quota: int = None,
        lni_sip_quota: int = None,
        node_id: str = None,
        region_id: str = None,
        v_switches: List[str] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # Lingjun Gaomi network interface controller quota
        self.hdeni_quota = hdeni_quota
        # Lingjun Elastic Network Interface quota, excluding system type
        self.leni_quota = leni_quota
        # Lingjun Elastic Network Interface Secondary Private IP Quota
        self.leni_sip_quota = leni_sip_quota
        # Lingjun network interface controller Secondary Private IP Quota
        self.lni_sip_quota = lni_sip_quota
        # The ID of the node for this operation.
        self.node_id = node_id
        # The region ID.
        self.region_id = region_id
        # List of VSwitches to which IP addresses can be applied for this node
        self.v_switches = v_switches
        # The ID of the Virtual Private Cloud to which the current node belongs.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.hdeni_quota is not None:
            result['HdeniQuota'] = self.hdeni_quota

        if self.leni_quota is not None:
            result['LeniQuota'] = self.leni_quota

        if self.leni_sip_quota is not None:
            result['LeniSipQuota'] = self.leni_sip_quota

        if self.lni_sip_quota is not None:
            result['LniSipQuota'] = self.lni_sip_quota

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('HdeniQuota') is not None:
            self.hdeni_quota = m.get('HdeniQuota')

        if m.get('LeniQuota') is not None:
            self.leni_quota = m.get('LeniQuota')

        if m.get('LeniSipQuota') is not None:
            self.leni_sip_quota = m.get('LeniSipQuota')

        if m.get('LniSipQuota') is not None:
            self.lni_sip_quota = m.get('LniSipQuota')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

