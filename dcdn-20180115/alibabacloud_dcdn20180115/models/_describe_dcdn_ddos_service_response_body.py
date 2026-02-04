# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnDdosServiceResponseBody(DaraModel):
    def __init__(
        self,
        changing_affect_time: str = None,
        changing_charge_type: str = None,
        changing_domian_num: int = None,
        changing_edition: str = None,
        changing_protect_num: int = None,
        charge_type: str = None,
        domian_num: int = None,
        edition: str = None,
        enabled: str = None,
        ending_time: str = None,
        instance_id: str = None,
        opening_time: str = None,
        protect_num: int = None,
        request_id: str = None,
        status: str = None,
    ):
        # The time when the renewed service takes effect. The time is displayed in UTC.
        self.changing_affect_time = changing_affect_time
        # The metering method after the configuration changes Valid values:
        # 
        # *   **PayByBandwidth**
        # *   **PayByTraffic**
        # *   **PayByBandwidth95**
        self.changing_charge_type = changing_charge_type
        # The number of protected domain names.
        self.changing_domian_num = changing_domian_num
        # The protection edition for which the configuration changes take effect. Valid values:
        # 
        # *   **poc**: POC Edition
        # *   **basic**: Basic Edition
        # *   **insurance**: Insurance Edition
        # *   **unlimited**: Unlimited Edition
        self.changing_edition = changing_edition
        # The number of mitigation sessions with configuration changes.
        self.changing_protect_num = changing_protect_num
        # The billing method. Valid values:
        # 
        # *   **PayByBandwidth**
        # *   **PayByTraffic**
        # *   **PayByBandwidth95**
        self.charge_type = charge_type
        # The number of protected domain names.
        self.domian_num = domian_num
        # The protection edition. Valid values:
        # 
        # *   **poc**: POC Edition
        # *   **basic**: Basic Edition
        # *   **insurance**: Insurance Edition
        # *   **unlimited**: Unlimited Edition
        self.edition = edition
        # The activation status of the service. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.enabled = enabled
        # The service expiration time.
        self.ending_time = ending_time
        # The instance ID.
        self.instance_id = instance_id
        # The time when the service was enabled.
        self.opening_time = opening_time
        # The number of mitigation sessions.
        self.protect_num = protect_num
        # The request ID.
        self.request_id = request_id
        # The status of the service. Valid values:
        # 
        # *   **Normal**
        # *   **WaitForExpire**
        # *   **expired**
        # *   **Released**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.changing_affect_time is not None:
            result['ChangingAffectTime'] = self.changing_affect_time

        if self.changing_charge_type is not None:
            result['ChangingChargeType'] = self.changing_charge_type

        if self.changing_domian_num is not None:
            result['ChangingDomianNum'] = self.changing_domian_num

        if self.changing_edition is not None:
            result['ChangingEdition'] = self.changing_edition

        if self.changing_protect_num is not None:
            result['ChangingProtectNum'] = self.changing_protect_num

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.domian_num is not None:
            result['DomianNum'] = self.domian_num

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.ending_time is not None:
            result['EndingTime'] = self.ending_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.opening_time is not None:
            result['OpeningTime'] = self.opening_time

        if self.protect_num is not None:
            result['ProtectNum'] = self.protect_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangingAffectTime') is not None:
            self.changing_affect_time = m.get('ChangingAffectTime')

        if m.get('ChangingChargeType') is not None:
            self.changing_charge_type = m.get('ChangingChargeType')

        if m.get('ChangingDomianNum') is not None:
            self.changing_domian_num = m.get('ChangingDomianNum')

        if m.get('ChangingEdition') is not None:
            self.changing_edition = m.get('ChangingEdition')

        if m.get('ChangingProtectNum') is not None:
            self.changing_protect_num = m.get('ChangingProtectNum')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DomianNum') is not None:
            self.domian_num = m.get('DomianNum')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('EndingTime') is not None:
            self.ending_time = m.get('EndingTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OpeningTime') is not None:
            self.opening_time = m.get('OpeningTime')

        if m.get('ProtectNum') is not None:
            self.protect_num = m.get('ProtectNum')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

