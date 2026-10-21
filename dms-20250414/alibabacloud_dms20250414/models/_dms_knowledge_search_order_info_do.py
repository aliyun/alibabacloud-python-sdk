# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DmsKnowledgeSearchOrderInfoDO(DaraModel):
    def __init__(
        self,
        aliyun_account_uid: str = None,
        api_key: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        order_id: str = None,
        web_search_api_url: str = None,
    ):
        self.aliyun_account_uid = aliyun_account_uid
        self.api_key = api_key
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.order_id = order_id
        self.web_search_api_url = web_search_api_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_account_uid is not None:
            result['AliyunAccountUid'] = self.aliyun_account_uid

        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.web_search_api_url is not None:
            result['WebSearchApiUrl'] = self.web_search_api_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunAccountUid') is not None:
            self.aliyun_account_uid = m.get('AliyunAccountUid')

        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('WebSearchApiUrl') is not None:
            self.web_search_api_url = m.get('WebSearchApiUrl')

        return self

