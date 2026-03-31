# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCompliancePackShrinkRequest(DaraModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        tag_shrink: str = None,
    ):
        # The ID of the compliance package.
        # 
        # For more information about how to obtain the ID of a compliance package, see [ListCompliancePacks](https://help.aliyun.com/document_detail/263332.html).
        # 
        # This parameter is required.
        self.compliance_pack_id = compliance_pack_id
        # The tags of the resource.
        # 
        # You can add up to 20 tags to a resource.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

