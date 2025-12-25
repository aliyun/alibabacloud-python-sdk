# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchDatabaseRequest(DaraModel):
    def __init__(
        self,
        db_type: str = None,
        env_type: str = None,
        page_number: int = None,
        page_size: int = None,
        real_login_user_uid: str = None,
        search_key: str = None,
        search_range: str = None,
        search_target: str = None,
        tid: int = None,
    ):
        # The type of the database. For more information about the valid values of this parameter, see [DbType parameter](https://help.aliyun.com/document_detail/198106.html).
        self.db_type = db_type
        # The environment type of the database. For more information, see [Change the environment type of an instance](https://help.aliyun.com/document_detail/163309.html).
        self.env_type = env_type
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        self.real_login_user_uid = real_login_user_uid
        # The keyword that is used to search for databases.
        self.search_key = search_key
        # The query range based on permissions. Valid values:
        # 
        # *   **HAS_PERMSSION**: searches for databases on which the current user has permissions.
        # *   **OWNER**: searches for databases owned by the current user.
        # *   **MY_FOCUS**: searches for databases that the current user follows.
        # *   **UNKNOWN**: searches for all databases.
        self.search_range = search_range
        # The category of the database. Valid values:
        # 
        # *   **DB**: single database or logical database.
        # *   **SINGLE_DB**: single database.
        # *   **LOGIC_DB**: logical database.
        self.search_target = search_target
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.real_login_user_uid is not None:
            result['RealLoginUserUid'] = self.real_login_user_uid

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.search_range is not None:
            result['SearchRange'] = self.search_range

        if self.search_target is not None:
            result['SearchTarget'] = self.search_target

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('SearchRange') is not None:
            self.search_range = m.get('SearchRange')

        if m.get('SearchTarget') is not None:
            self.search_target = m.get('SearchTarget')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

