# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TemplateRecord(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        copy_status: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        template_id: str = None,
        user_id: str = None,
    ):
        self.biz_id = biz_id
        self.copy_status = copy_status
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_create = gmt_create
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_modified = gmt_modified
        self.id = id
        self.template_id = template_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.copy_status is not None:
            result['CopyStatus'] = self.copy_status

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('CopyStatus') is not None:
            self.copy_status = m.get('CopyStatus')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

