# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateAliyunCertUrlRequest(DaraModel):
    def __init__(
        self,
        aliyun_pk: str = None,
        app_name: str = None,
        apply_channel: str = None,
        apply_type: str = None,
        callback: str = None,
        cert_way: str = None,
        ignore_already_cert: bool = None,
        is_mobile: bool = None,
        is_open_app: bool = None,
        platform: str = None,
        source: str = None,
        subject_type: str = None,
    ):
        # This parameter is required.
        self.aliyun_pk = aliyun_pk
        # This parameter is required.
        self.app_name = app_name
        self.apply_channel = apply_channel
        self.apply_type = apply_type
        self.callback = callback
        self.cert_way = cert_way
        self.ignore_already_cert = ignore_already_cert
        self.is_mobile = is_mobile
        self.is_open_app = is_open_app
        # This parameter is required.
        self.platform = platform
        # This parameter is required.
        self.source = source
        # This parameter is required.
        self.subject_type = subject_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_pk is not None:
            result['AliyunPk'] = self.aliyun_pk

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.apply_channel is not None:
            result['ApplyChannel'] = self.apply_channel

        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type

        if self.callback is not None:
            result['Callback'] = self.callback

        if self.cert_way is not None:
            result['CertWay'] = self.cert_way

        if self.ignore_already_cert is not None:
            result['IgnoreAlreadyCert'] = self.ignore_already_cert

        if self.is_mobile is not None:
            result['IsMobile'] = self.is_mobile

        if self.is_open_app is not None:
            result['IsOpenApp'] = self.is_open_app

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.source is not None:
            result['Source'] = self.source

        if self.subject_type is not None:
            result['SubjectType'] = self.subject_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunPk') is not None:
            self.aliyun_pk = m.get('AliyunPk')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ApplyChannel') is not None:
            self.apply_channel = m.get('ApplyChannel')

        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')

        if m.get('Callback') is not None:
            self.callback = m.get('Callback')

        if m.get('CertWay') is not None:
            self.cert_way = m.get('CertWay')

        if m.get('IgnoreAlreadyCert') is not None:
            self.ignore_already_cert = m.get('IgnoreAlreadyCert')

        if m.get('IsMobile') is not None:
            self.is_mobile = m.get('IsMobile')

        if m.get('IsOpenApp') is not None:
            self.is_open_app = m.get('IsOpenApp')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SubjectType') is not None:
            self.subject_type = m.get('SubjectType')

        return self

