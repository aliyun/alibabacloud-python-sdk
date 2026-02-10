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
        # The information about the vulnerability. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   namespace: the namespace of the image
        # *   repoName: the name of the Container Registry repository
        # *   regionId: the region ID
        # *   instanceId: the ID of the Container Registry instance
        # *   repoId: the name of the repository
        # *   tag: the tad added to the image
        # *   digest: the digest of the image
        # *   newTag: the tag added to the image after the vulnerability is fixed
        # *   uuid: the UUID of the image
        # *   ids: the IDs of the vulnerability primary keys
        self.info = info
        # If you want to fix the vulnerability, set the value to vul_fix.
        self.operate_type = operate_type
        # The type of the vulnerability. Set the value to cve.
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

