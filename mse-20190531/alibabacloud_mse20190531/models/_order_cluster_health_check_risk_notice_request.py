# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OrderClusterHealthCheckRiskNoticeRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
        mute: bool = None,
        notice_type: str = None,
        region_id: str = None,
        request_pars: str = None,
        risk_code: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the instance.
        self.instance_id = instance_id
        # Specifies whether to disable the notification feature if the risk item occurs.
        # 
        # *   true: disabled
        # *   false: enabled
        self.mute = mute
        # A reserved parameter.
        self.notice_type = notice_type
        # The region in which the cluster resides.
        self.region_id = region_id
        # The extended request parameters in the JSON format.
        self.request_pars = request_pars
        # The ID of the risk item.
        self.risk_code = risk_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mute is not None:
            result['Mute'] = self.mute

        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        if self.risk_code is not None:
            result['RiskCode'] = self.risk_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mute') is not None:
            self.mute = m.get('Mute')

        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        if m.get('RiskCode') is not None:
            self.risk_code = m.get('RiskCode')

        return self

