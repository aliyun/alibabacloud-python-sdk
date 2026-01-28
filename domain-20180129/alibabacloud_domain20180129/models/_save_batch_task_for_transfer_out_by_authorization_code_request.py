# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class SaveBatchTaskForTransferOutByAuthorizationCodeRequest(DaraModel):
    def __init__(
        self,
        transfer_out_param_list: List[main_models.SaveBatchTaskForTransferOutByAuthorizationCodeRequestTransferOutParamList] = None,
    ):
        # This parameter is required.
        self.transfer_out_param_list = transfer_out_param_list

    def validate(self):
        if self.transfer_out_param_list:
            for v1 in self.transfer_out_param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TransferOutParamList'] = []
        if self.transfer_out_param_list is not None:
            for k1 in self.transfer_out_param_list:
                result['TransferOutParamList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.transfer_out_param_list = []
        if m.get('TransferOutParamList') is not None:
            for k1 in m.get('TransferOutParamList'):
                temp_model = main_models.SaveBatchTaskForTransferOutByAuthorizationCodeRequestTransferOutParamList()
                self.transfer_out_param_list.append(temp_model.from_map(k1))

        return self

class SaveBatchTaskForTransferOutByAuthorizationCodeRequestTransferOutParamList(DaraModel):
    def __init__(
        self,
        authorization_code: str = None,
        domain_name: str = None,
    ):
        self.authorization_code = authorization_code
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_code is not None:
            result['AuthorizationCode'] = self.authorization_code

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationCode') is not None:
            self.authorization_code = m.get('AuthorizationCode')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        return self

