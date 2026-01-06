# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeNfsAclResponseBody(DaraModel):
    def __init__(
        self,
        acl: main_models.DescribeNfsAclResponseBodyAcl = None,
        request_id: str = None,
    ):
        # The information about the ACL feature.
        self.acl = acl
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.acl:
            self.acl.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['Acl'] = self.acl.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acl') is not None:
            temp_model = main_models.DescribeNfsAclResponseBodyAcl()
            self.acl = temp_model.from_map(m.get('Acl'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNfsAclResponseBodyAcl(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Indicates whether the NFS ACL feature is enabled.
        # 
        # *   true: The NFS ACL feature is enabled.
        # *   false: The NFS ACL feature is disabled.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

