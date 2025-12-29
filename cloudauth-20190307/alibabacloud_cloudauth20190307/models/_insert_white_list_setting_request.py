# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertWhiteListSettingRequest(DaraModel):
    def __init__(
        self,
        cert_no: str = None,
        certify_id: str = None,
        remark: str = None,
        scene_id: int = None,
        service_code: str = None,
        valid_day: int = None,
    ):
        # ID number.
        self.cert_no = cert_no
        # Unique identifier for real person authentication.
        self.certify_id = certify_id
        # Remark, with a length less than 32 characters.
        self.remark = remark
        # Authentication scene ID. This ID is automatically generated after creating an authentication scene in the console. For instructions on how to create an authentication scene, see Adding an Authentication Scene.
        self.scene_id = scene_id
        # ServiceCode for the real person cloud product, value: **antcloudauth**.
        self.service_code = service_code
        # Whitelist validity period in days (only supports 3, 7, 30).
        self.valid_day = valid_day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no

        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.valid_day is not None:
            result['ValidDay'] = self.valid_day

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')

        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('ValidDay') is not None:
            self.valid_day = m.get('ValidDay')

        return self

