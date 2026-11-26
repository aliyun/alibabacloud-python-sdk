# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPrimaryObjectDataRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        keyword: str = None,
        only_favorites: bool = None,
        operating_object_name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        page: int = None,
        page_size: int = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The keyword for search. The keyword is matched against the name field. If the schema defines a description field, the keyword is also matched against the description field.
        self.keyword = keyword
        # Specifies whether to return only favorited primary objects. If this parameter is set to false or not specified, all objects are returned, including the isFavorited flag.
        self.only_favorites = only_favorites
        # The operating object name, such as customer_1.
        # 
        # This parameter is required.
        self.operating_object_name = operating_object_name
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The page number. Pages start from page 1.
        self.page = page
        # The number of entries per page. Valid values: 1 to 100.
        self.page_size = page_size
        # The tenant ID. This is a common parameter. You can explicitly pass this parameter by using --tenant-id in winnexo-cli.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.only_favorites is not None:
            result['onlyFavorites'] = self.only_favorites

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('onlyFavorites') is not None:
            self.only_favorites = m.get('onlyFavorites')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

