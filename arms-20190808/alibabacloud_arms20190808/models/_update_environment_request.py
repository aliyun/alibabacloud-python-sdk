# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEnvironmentRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        environment_id: str = None,
        environment_name: str = None,
        fee_package: str = None,
        region_id: str = None,
    ):
        # The language. Valid values: zh and en. Default value: zh.
        self.aliyun_lang = aliyun_lang
        # The environment ID.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The name of the environment instance.
        self.environment_name = environment_name
        # The payable resource plan. Valid values:
        # 
        # *   If the EnvironmentType parameter is set to CS, set the value to CS_Basic or CS_Pro. Default value: CS_Basic.
        # *   Otherwise, leave the parameter empty.
        self.fee_package = fee_package
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.environment_name is not None:
            result['EnvironmentName'] = self.environment_name

        if self.fee_package is not None:
            result['FeePackage'] = self.fee_package

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('EnvironmentName') is not None:
            self.environment_name = m.get('EnvironmentName')

        if m.get('FeePackage') is not None:
            self.fee_package = m.get('FeePackage')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

