# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyEventStatusRequest(DaraModel):
    def __init__(
        self,
        backed: bool = None,
        deal_reason: str = None,
        id: int = None,
        lang: str = None,
        status: int = None,
    ):
        # Specifies whether to enhance the detection of anomalous events. If you enhance the detection of anomalous events, the detection accuracy and the rate of triggering alerts for anomalous events are improved. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.backed = backed
        # The reason why the anomalous event is handled.
        self.deal_reason = deal_reason
        # The ID of the anomalous event.
        # 
        # > You can call the **DescribeEvents** operation to query the ID of the anomalous event.
        # 
        # This parameter is required.
        self.id = id
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang
        # The method to handle the anomalous event. Valid values:
        # 
        # *   **1**: marks the anomalous event as a false positive.
        # *   **2**: confirms and handles the anomalous event.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backed is not None:
            result['Backed'] = self.backed

        if self.deal_reason is not None:
            result['DealReason'] = self.deal_reason

        if self.id is not None:
            result['Id'] = self.id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Backed') is not None:
            self.backed = m.get('Backed')

        if m.get('DealReason') is not None:
            self.deal_reason = m.get('DealReason')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

