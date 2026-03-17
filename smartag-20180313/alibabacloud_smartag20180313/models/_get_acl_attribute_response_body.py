# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAclAttributeResponseBody(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_name: str = None,
        error_config_smart_agcount: int = None,
        request_id: str = None,
    ):
        # The ID of the ACL.
        self.acl_id = acl_id
        # The name of the ACL.
        self.acl_name = acl_name
        # The number of SAG devices that are associated with the ACL who has DPI configuration errors.
        # 
        # You can call the [ListDpiConfigError](https://help.aliyun.com/document_detail/197566.html) operation to query exception details and SAG device information.
        self.error_config_smart_agcount = error_config_smart_agcount
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_name is not None:
            result['AclName'] = self.acl_name

        if self.error_config_smart_agcount is not None:
            result['ErrorConfigSmartAGCount'] = self.error_config_smart_agcount

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')

        if m.get('ErrorConfigSmartAGCount') is not None:
            self.error_config_smart_agcount = m.get('ErrorConfigSmartAGCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

