# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMgsApipageRequest(DaraModel):
    def __init__(
        self,
        api_status: str = None,
        api_type: str = None,
        app_id: str = None,
        format: str = None,
        host: str = None,
        need_encrypt: str = None,
        need_etag: str = None,
        need_sign: str = None,
        operation_type: str = None,
        opt_fuzzy: str = None,
        page_index: int = None,
        page_size: int = None,
        sys_id: int = None,
        sys_name: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.api_status = api_status
        self.api_type = api_type
        self.app_id = app_id
        self.format = format
        self.host = host
        self.need_encrypt = need_encrypt
        self.need_etag = need_etag
        self.need_sign = need_sign
        self.operation_type = operation_type
        self.opt_fuzzy = opt_fuzzy
        self.page_index = page_index
        self.page_size = page_size
        self.sys_id = sys_id
        self.sys_name = sys_name
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_status is not None:
            result['ApiStatus'] = self.api_status

        if self.api_type is not None:
            result['ApiType'] = self.api_type

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.format is not None:
            result['Format'] = self.format

        if self.host is not None:
            result['Host'] = self.host

        if self.need_encrypt is not None:
            result['NeedEncrypt'] = self.need_encrypt

        if self.need_etag is not None:
            result['NeedEtag'] = self.need_etag

        if self.need_sign is not None:
            result['NeedSign'] = self.need_sign

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.opt_fuzzy is not None:
            result['OptFuzzy'] = self.opt_fuzzy

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sys_id is not None:
            result['SysId'] = self.sys_id

        if self.sys_name is not None:
            result['SysName'] = self.sys_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiStatus') is not None:
            self.api_status = m.get('ApiStatus')

        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('NeedEncrypt') is not None:
            self.need_encrypt = m.get('NeedEncrypt')

        if m.get('NeedEtag') is not None:
            self.need_etag = m.get('NeedEtag')

        if m.get('NeedSign') is not None:
            self.need_sign = m.get('NeedSign')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('OptFuzzy') is not None:
            self.opt_fuzzy = m.get('OptFuzzy')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SysId') is not None:
            self.sys_id = m.get('SysId')

        if m.get('SysName') is not None:
            self.sys_name = m.get('SysName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

