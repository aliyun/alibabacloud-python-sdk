# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWhitelistSettingRequest(DaraModel):
    def __init__(
        self,
        cert_no: str = None,
        certify_id: str = None,
        lang: str = None,
        remark: str = None,
        scene_id: int = None,
        service_code: str = None,
        source_ip: str = None,
        valid_day: int = None,
    ):
        # ID number to be whitelisted.
        self.cert_no = cert_no
        # Certificate ID, used for whitelisting this specific authenticated user.
        self.certify_id = certify_id
        # User language.
        self.lang = lang
        # Whitelist remarks.
        self.remark = remark
        # Scene ID.
        self.scene_id = scene_id
        # Service type:
        # - **antcloudauth**: Financial-grade real-person authentication.
        # - **cloudauthst** (discontinued): Enhanced real-person authentication.
        # 
        # This parameter is required.
        self.service_code = service_code
        # Visitor\\"s source IP address. No need to fill in, the system will automatically obtain it.
        self.source_ip = source_ip
        # Number of valid days after creating the whitelist.
        # 
        # This parameter is required.
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

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.valid_day is not None:
            result['ValidDay'] = self.valid_day

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')

        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('ValidDay') is not None:
            self.valid_day = m.get('ValidDay')

        return self

