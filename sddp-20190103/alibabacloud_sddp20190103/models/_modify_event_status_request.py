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
        # Specifies whether to enhance the detection of the anomalous activity. Enhancing detection improves accuracy and increases the alert rate for anomalous activities.
        # 
        # - **true**: Yes.
        # 
        # - **false**: No.
        self.backed = backed
        # The reason for handling the anomalous activity.
        self.deal_reason = deal_reason
        # The unique ID of the anomalous activity.
        # 
        # > To handle an anomalous activity, you must provide its unique ID. You can obtain this ID by calling the **DescribeEvents** operation.
        # 
        # This parameter is required.
        self.id = id
        # The language of the request and response. The default value is **zh_cn**. Valid values:
        # 
        # - **zh_cn**: Chinese.
        # 
        # - **en_us**: English.
        self.lang = lang
        # The operation to perform on the anomalous activity.
        # 
        # - **1**: Mark as false positive.
        # 
        # - **2**: Confirm and handle the anomalous activity.
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

