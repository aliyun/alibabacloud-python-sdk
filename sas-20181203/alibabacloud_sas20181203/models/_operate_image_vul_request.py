# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateImageVulRequest(DaraModel):
    def __init__(
        self,
        info: str = None,
        operate_type: str = None,
        type: str = None,
    ):
        # The information about the vulnerability to be processed. This parameter is in JSON format and contains the following fields:
        # 
        # - namespace: the image namespace.
        # - repoName: the name of the ACR image repository.
        # - regionId: the region.
        # - instanceId: the ID of the ACR instance.
        # - repoId: the ID of the repository.
        # - tag: the original tag of the image.
        # - digest: the digest of the image.
        # - newTag: the tag of the image after the fix.
        # - uuid: the UUID of the image.
        # - ids: the list of primary key IDs of the vulnerabilities.
        self.info = info
        # The operation type for image vulnerability fix. Set this parameter to vul_fix.
        self.operate_type = operate_type
        # The vulnerability type. Set this parameter to cve.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info is not None:
            result['Info'] = self.info

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

