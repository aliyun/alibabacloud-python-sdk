# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetChatFlowMetricRequest(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_code: str = None,
        flow_version: str = None,
        from_: int = None,
        metric_name: str = None,
        metric_param: Dict[str, Any] = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        to: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Flow code.
        self.flow_code = flow_code
        # Flow version.
        self.flow_version = flow_version
        # Start timestamp in seconds.
        self.from_ = from_
        # Metric name.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        self.metric_param = metric_param
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # End timestamp in seconds.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend

        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code

        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version

        if self.from_ is not None:
            result['From'] = self.from_

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.metric_param is not None:
            result['MetricParam'] = self.metric_param

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')

        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')

        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('MetricParam') is not None:
            self.metric_param = m.get('MetricParam')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

