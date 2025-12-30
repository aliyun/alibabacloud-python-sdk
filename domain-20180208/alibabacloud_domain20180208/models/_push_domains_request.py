# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PushDomainsRequest(DaraModel):
    def __init__(
        self,
        domain_list: List[str] = None,
        out_biz_id: str = None,
        publish_remark: str = None,
        receiver_account: str = None,
    ):
        # This parameter is required.
        self.domain_list = domain_list
        # This parameter is required.
        self.out_biz_id = out_biz_id
        self.publish_remark = publish_remark
        # This parameter is required.
        self.receiver_account = receiver_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list

        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id

        if self.publish_remark is not None:
            result['PublishRemark'] = self.publish_remark

        if self.receiver_account is not None:
            result['ReceiverAccount'] = self.receiver_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')

        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')

        if m.get('PublishRemark') is not None:
            self.publish_remark = m.get('PublishRemark')

        if m.get('ReceiverAccount') is not None:
            self.receiver_account = m.get('ReceiverAccount')

        return self

