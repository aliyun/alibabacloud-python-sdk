# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBandWithdChargeTypeResponseBody(DaraModel):
    def __init__(
        self,
        band_with_type_info: str = None,
        charge_contract_type: str = None,
        charge_cycle_info: str = None,
        code: int = None,
        request_id: str = None,
    ):
        # The information about the metering method.
        self.band_with_type_info = band_with_type_info
        # The metering type.
        # 
        # *   ChargeByUnified: unified metering.
        # *   ChargeByGrade: differential metering.
        self.charge_contract_type = charge_contract_type
        # The metering cycle. Currently, this parameter is empty in the response.
        self.charge_cycle_info = charge_cycle_info
        # The returned service code. A value of 0 indicates that the operation was successful.
        self.code = code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.band_with_type_info is not None:
            result['BandWithTypeInfo'] = self.band_with_type_info

        if self.charge_contract_type is not None:
            result['ChargeContractType'] = self.charge_contract_type

        if self.charge_cycle_info is not None:
            result['ChargeCycleInfo'] = self.charge_cycle_info

        if self.code is not None:
            result['Code'] = self.code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWithTypeInfo') is not None:
            self.band_with_type_info = m.get('BandWithTypeInfo')

        if m.get('ChargeContractType') is not None:
            self.charge_contract_type = m.get('ChargeContractType')

        if m.get('ChargeCycleInfo') is not None:
            self.charge_cycle_info = m.get('ChargeCycleInfo')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

