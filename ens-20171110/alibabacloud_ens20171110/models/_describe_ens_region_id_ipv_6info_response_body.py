# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEnsRegionIdIpv6InfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        support_ipv_6info: main_models.DescribeEnsRegionIdIpv6InfoResponseBodySupportIpv6Info = None,
    ):
        # The request ID.
        self.request_id = request_id
        # IPv6 support information.
        self.support_ipv_6info = support_ipv_6info

    def validate(self):
        if self.support_ipv_6info:
            self.support_ipv_6info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.support_ipv_6info is not None:
            result['SupportIpv6Info'] = self.support_ipv_6info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SupportIpv6Info') is not None:
            temp_model = main_models.DescribeEnsRegionIdIpv6InfoResponseBodySupportIpv6Info()
            self.support_ipv_6info = temp_model.from_map(m.get('SupportIpv6Info'))

        return self

class DescribeEnsRegionIdIpv6InfoResponseBodySupportIpv6Info(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        support_ipv_6: bool = None,
    ):
        # The ID of the node.
        self.ens_region_id = ens_region_id
        # Specifies whether IPv6 is supported. Valid values:
        # 
        # *   true
        # *   false
        self.support_ipv_6 = support_ipv_6

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.support_ipv_6 is not None:
            result['SupportIpv6'] = self.support_ipv_6

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('SupportIpv6') is not None:
            self.support_ipv_6 = m.get('SupportIpv6')

        return self

