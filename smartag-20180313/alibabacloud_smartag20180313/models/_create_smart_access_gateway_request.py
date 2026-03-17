# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSmartAccessGatewayRequest(DaraModel):
    def __init__(
        self,
        already_have_sag: bool = None,
        auto_pay: bool = None,
        buyer_message: str = None,
        cpeversion: str = None,
        charge_type: str = None,
        description: str = None,
        ha_type: str = None,
        hard_ware_spec: str = None,
        max_band_width: int = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        receiver_address: str = None,
        receiver_city: str = None,
        receiver_country: str = None,
        receiver_district: str = None,
        receiver_email: str = None,
        receiver_mobile: str = None,
        receiver_name: str = None,
        receiver_phone: str = None,
        receiver_state: str = None,
        receiver_town: str = None,
        receiver_zip: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether you already have an SAG device. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.already_have_sag = already_have_sag
        # Specifies whether to enable auto-payment for the instance. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # If you set the parameter to false, go to Billing Management to complete the payment after you call this operation. After you complete the payment, the instance can be created.
        # 
        # This parameter is required.
        self.auto_pay = auto_pay
        # The remarks left by the buyer.
        # 
        # This parameter is required.
        self.buyer_message = buyer_message
        # The edition of SAG when you create an SAG vCPE instance.
        # 
        # Set the value to **basic**, which specifies Basic Edition.
        self.cpeversion = cpeversion
        # The billing method of the SAG instance.
        # 
        # Set the value to **PREPAY**, which specifies the subscription billing method.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The description of the SAG instance.
        # 
        # The description must be 2 to 256 characters in length, and can contain digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        self.description = description
        # The deployment mode. Valid values:
        # 
        # *   **no_backup**: You buy only one SAG device to connect private networks to Alibaba Cloud.
        # *   **cold_backup**: You buy two SAG devices in active-standby mode. One SAG device serves as an active device and the other serves as a standby device. Only the active device is connected to Alibaba Cloud. If the active device is not working as expected, you must manually perform a switchover.
        # *   **warm_backup**: You buy two SAG devices in active-active mode. Both SAG devices are connected to Alibaba Cloud. If an active device is not working as expected, a failover is automatically performed.
        # 
        # >  If you want to create an SAG vCPE instance, set the value to **warm_backup**.
        # 
        # This parameter is required.
        self.ha_type = ha_type
        # The type of the SAG instance. Valid values:
        # 
        # *   **sag-100wm**
        # *   **sag-1000**
        # *   **sag-vcpe**
        # 
        # This parameter is required.
        self.hard_ware_spec = hard_ware_spec
        # The bandwidth of the SAG instance.
        # 
        # *   If you want to create an SAG CPE instance and the model is **sag-100wm**, valid values of this parameter are **2** to **50**. Unit: Mbit/s.
        # *   If you want to create an SAG CPE instance and the model is **sag-1000**, valid values of this parameter are **10** to **500**. Unit: Mbit/s.
        # *   If you want to create an SAG vCPE instance, valid values of this parameter are **10** to **1000**. Unit: Mbit/s.
        self.max_band_width = max_band_width
        # The name of the SAG instance.
        # 
        # The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription period of the SAG instance. Unit: months.
        # 
        # Valid values: **1** to **9**, **12**, **24**, and **36**.
        # 
        # This parameter is required.
        self.period = period
        # The detailed address of the recipient.
        # 
        # This parameter is required.
        self.receiver_address = receiver_address
        # The city of the recipient address.
        # 
        # This parameter is required.
        self.receiver_city = receiver_city
        # The country of the recipient address.
        # 
        # This parameter is required.
        self.receiver_country = receiver_country
        # The district of the recipient address.
        # 
        # This parameter is required.
        self.receiver_district = receiver_district
        # The email address of the recipient.
        # 
        # This parameter is required.
        self.receiver_email = receiver_email
        # The mobile phone number of the recipient.
        # 
        # This parameter is required.
        self.receiver_mobile = receiver_mobile
        # The name of the recipient.
        # 
        # This parameter is required.
        self.receiver_name = receiver_name
        # The landline phone number of the recipient.
        self.receiver_phone = receiver_phone
        # The province of the recipient address.
        # 
        # This parameter is required.
        self.receiver_state = receiver_state
        # The town of the recipient address.
        # 
        # This parameter is required.
        self.receiver_town = receiver_town
        # The postcode of the recipient address.
        # 
        # This parameter is required.
        self.receiver_zip = receiver_zip
        # The ID of the region where you want to deploy the SAG instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.already_have_sag is not None:
            result['AlreadyHaveSag'] = self.already_have_sag

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.buyer_message is not None:
            result['BuyerMessage'] = self.buyer_message

        if self.cpeversion is not None:
            result['CPEVersion'] = self.cpeversion

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.description is not None:
            result['Description'] = self.description

        if self.ha_type is not None:
            result['HaType'] = self.ha_type

        if self.hard_ware_spec is not None:
            result['HardWareSpec'] = self.hard_ware_spec

        if self.max_band_width is not None:
            result['MaxBandWidth'] = self.max_band_width

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.receiver_address is not None:
            result['ReceiverAddress'] = self.receiver_address

        if self.receiver_city is not None:
            result['ReceiverCity'] = self.receiver_city

        if self.receiver_country is not None:
            result['ReceiverCountry'] = self.receiver_country

        if self.receiver_district is not None:
            result['ReceiverDistrict'] = self.receiver_district

        if self.receiver_email is not None:
            result['ReceiverEmail'] = self.receiver_email

        if self.receiver_mobile is not None:
            result['ReceiverMobile'] = self.receiver_mobile

        if self.receiver_name is not None:
            result['ReceiverName'] = self.receiver_name

        if self.receiver_phone is not None:
            result['ReceiverPhone'] = self.receiver_phone

        if self.receiver_state is not None:
            result['ReceiverState'] = self.receiver_state

        if self.receiver_town is not None:
            result['ReceiverTown'] = self.receiver_town

        if self.receiver_zip is not None:
            result['ReceiverZip'] = self.receiver_zip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlreadyHaveSag') is not None:
            self.already_have_sag = m.get('AlreadyHaveSag')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('BuyerMessage') is not None:
            self.buyer_message = m.get('BuyerMessage')

        if m.get('CPEVersion') is not None:
            self.cpeversion = m.get('CPEVersion')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HaType') is not None:
            self.ha_type = m.get('HaType')

        if m.get('HardWareSpec') is not None:
            self.hard_ware_spec = m.get('HardWareSpec')

        if m.get('MaxBandWidth') is not None:
            self.max_band_width = m.get('MaxBandWidth')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('ReceiverAddress') is not None:
            self.receiver_address = m.get('ReceiverAddress')

        if m.get('ReceiverCity') is not None:
            self.receiver_city = m.get('ReceiverCity')

        if m.get('ReceiverCountry') is not None:
            self.receiver_country = m.get('ReceiverCountry')

        if m.get('ReceiverDistrict') is not None:
            self.receiver_district = m.get('ReceiverDistrict')

        if m.get('ReceiverEmail') is not None:
            self.receiver_email = m.get('ReceiverEmail')

        if m.get('ReceiverMobile') is not None:
            self.receiver_mobile = m.get('ReceiverMobile')

        if m.get('ReceiverName') is not None:
            self.receiver_name = m.get('ReceiverName')

        if m.get('ReceiverPhone') is not None:
            self.receiver_phone = m.get('ReceiverPhone')

        if m.get('ReceiverState') is not None:
            self.receiver_state = m.get('ReceiverState')

        if m.get('ReceiverTown') is not None:
            self.receiver_town = m.get('ReceiverTown')

        if m.get('ReceiverZip') is not None:
            self.receiver_zip = m.get('ReceiverZip')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

