# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAutoAuditUnblockRequest(DaraModel):
    def __init__(
        self,
        asset_list: str = None,
        auditor: str = None,
        customer_uid: str = None,
        email_type: str = None,
        has_unsubscribe: bool = None,
        send_count: str = None,
        use_desc: str = None,
    ):
        self.asset_list = asset_list
        self.auditor = auditor
        self.customer_uid = customer_uid
        self.email_type = email_type
        self.has_unsubscribe = has_unsubscribe
        self.send_count = send_count
        self.use_desc = use_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_list is not None:
            result['AssetList'] = self.asset_list

        if self.auditor is not None:
            result['Auditor'] = self.auditor

        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid

        if self.email_type is not None:
            result['EmailType'] = self.email_type

        if self.has_unsubscribe is not None:
            result['HasUnsubscribe'] = self.has_unsubscribe

        if self.send_count is not None:
            result['SendCount'] = self.send_count

        if self.use_desc is not None:
            result['UseDesc'] = self.use_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')

        if m.get('Auditor') is not None:
            self.auditor = m.get('Auditor')

        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')

        if m.get('EmailType') is not None:
            self.email_type = m.get('EmailType')

        if m.get('HasUnsubscribe') is not None:
            self.has_unsubscribe = m.get('HasUnsubscribe')

        if m.get('SendCount') is not None:
            self.send_count = m.get('SendCount')

        if m.get('UseDesc') is not None:
            self.use_desc = m.get('UseDesc')

        return self

