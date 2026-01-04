# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        data_disk: List[main_models.CreateInstanceRequestDataDisk] = None,
        system_disk: main_models.CreateInstanceRequestSystemDisk = None,
        auto_renew: str = None,
        auto_renew_period: str = None,
        ens_region_id: str = None,
        host_name: str = None,
        image_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        ip_type: str = None,
        key_pair_name: str = None,
        owner_id: int = None,
        password: str = None,
        password_inherit: bool = None,
        payment_type: str = None,
        period: str = None,
        private_ip_address: str = None,
        public_ip_identification: bool = None,
        quantity: str = None,
        unique_suffix: bool = None,
        user_data: str = None,
        v_switch_id: str = None,
    ):
        self.data_disk = data_disk
        self.system_disk = system_disk
        # Specifies whether to enable the auto-renewal feature. Valid values: **True** and **False**. Default value: False.
        self.auto_renew = auto_renew
        # The auto-renewal period for the instance. This parameter is required when the **AutoRenew** parameter is set to **True**. Valid values: **1** to **12**. Unit: months.
        self.auto_renew_period = auto_renew_period
        # The region ID.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The hostname of the Elastic Compute Service (ECS) instance. General naming rules: The hostname cannot start or end with a period (.) or hyphen (-). It cannot contain consecutive periods (.) or hyphens (-).
        # 
        # Naming rules for specific instances:
        # 
        # *   For Windows instances, the hostname must be **2** to **15** characters in length and cannot contain periods (.) or contain only digits. The hostname cannot contain periods (.) or contain only digits.
        # *   For instances that run one of other operating systems such as Linux, the hostname must be **2** to **64** characters in length. You can use periods (.) to separate the hostname into multiple segments. Each segment can contain letters, digits, and hyphens (-).
        self.host_name = host_name
        # The ID of the image file that you select when creating the instance.
        self.image_id = image_id
        # The name of the instance. The name must conform to the following naming conventions:
        # 
        # *   The name must be **2** to **128** characters in length.
        # *   It must start with a letter but cannot start with http:// or https://.
        # *   The name can contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # If you do not specify this parameter, the instance ID is used as the instance name by default.
        self.instance_name = instance_name
        # The type of the instance.
        # 
        # For more information, see [](~~66124~~).
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # This parameter is required if you create the instance for the first time. The existing billing method is used by default if you have created an instance. Valid values:
        # 
        # *   **BandwidthByDay**: Pay by daily peak bandwidth.
        # *   **95BandwidthByMonth**: Pay by monthly 95th percentile bandwidth.
        self.internet_charge_type = internet_charge_type
        # The type of the IP address. Valid values:
        # 
        # *   **ipv4** (default)
        # *   **ipv6**
        # *   **ipv4Andipv6**
        self.ip_type = ip_type
        # The name of the key pair. You can specify only one name.
        self.key_pair_name = key_pair_name
        self.owner_id = owner_id
        # The password of the instance.
        # 
        # The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include: ``()`~!@#$%^&*-_+=|{}[]:;\\"<>,.?/``
        self.password = password
        # Specifies whether to use the preset password of the image. Valid values:
        # 
        # - **true**: The password preset in the image is used, and the **Password** parameter must be null. For secure access, make sure that the selected image has a password configured.
        # 
        # - **false**: does not use the password preset in the image.
        self.password_inherit = password_inherit
        # The billing method of the instance. Set the value to Subscription.
        self.payment_type = payment_type
        # The subscription period of the instance. Valid values: **1** to **9** and **12**. Unit: months.
        # 
        # This parameter is required.
        self.period = period
        # The internal IP address. If this parameter is specified, you must specify the vSwitch ID. The vSwitch must be created first. Otherwise, an error is returned.
        self.private_ip_address = private_ip_address
        # Specifies whether a public IP address can be assigned to the specified instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.public_ip_identification = public_ip_identification
        # The number of instances.
        # 
        # This parameter is required.
        self.quantity = quantity
        # Specifies whether to automatically append sequential suffixes to the hostnames specified by the **HostName** parameter and instance names specified by the **InstanceName** parameter. The sequential suffixes range from **001** to **999**.
        # 
        # Examples: **LocalHost001** and **LocalHost002**, and **MyInstance001** and **MyInstance002**.
        # 
        # Default value: **false**.
        self.unique_suffix = unique_suffix
        # Custom data. The data starts with `#!`. The data can be at most 256 characters in length and 16 KB in size. Only custom scripts are supported and cannot be rendered by InstanceMetaData.
        # 
        # You can specify custom data. The data is encoded in Base64. The system does not encrypt your custom data when API requests are initiated. We recommend that you do not pass in confidential information such as passwords and private keys in plaintext. If you want to provide sensitive data such as passwords and private keys, encrypt the data and then encode it in Base64. The data is decrypted on the instance in the way it is encrypted.
        # 
        # For more information, see [User data formats](https://cloudinit.readthedocs.io/en/latest/topics/format.html).
        self.user_data = user_data
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.data_disk:
            for v1 in self.data_disk:
                 if v1:
                    v1.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.period is not None:
            result['Period'] = self.period

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.public_ip_identification is not None:
            result['PublicIpIdentification'] = self.public_ip_identification

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.unique_suffix is not None:
            result['UniqueSuffix'] = self.unique_suffix

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.CreateInstanceRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('SystemDisk') is not None:
            temp_model = main_models.CreateInstanceRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('PublicIpIdentification') is not None:
            self.public_ip_identification = m.get('PublicIpIdentification')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('UniqueSuffix') is not None:
            self.unique_suffix = m.get('UniqueSuffix')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class CreateInstanceRequestSystemDisk(DaraModel):
    def __init__(
        self,
        size: str = None,
    ):
        # The size of the system disk. Unit: GiB. Valid values: **20** and **40**. The value cannot be smaller than the size of the image and must be a multiple of 10 GiB.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class CreateInstanceRequestDataDisk(DaraModel):
    def __init__(
        self,
        size: str = None,
    ):
        # The capacity of the first data disk. Unit: GiB. The capacity is at least 20 GiB and is a multiple of 10 GiB.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

