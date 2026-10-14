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
        # Specifies whether to enable auto-renewal. Valid values: **True** | **False** (default).
        self.auto_renew = auto_renew
        # The auto-renewal period. This parameter is required when **AutoRenew** is set to **True**. Valid values: **1** to **12**. Unit: months.
        self.auto_renew_period = auto_renew_period
        # The region ID.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The hostname of the instance.
        # General naming conventions: Periods (.) and hyphens (-) cannot be used as the first or last character and cannot be used consecutively.
        # 
        # Specific naming conventions:
        # - Windows instances: The hostname must be **2** to **15** characters in length. Periods (.) are not supported. The hostname cannot consist entirely of digits. Uppercase letters, lowercase letters, digits, and hyphens (-) are allowed.
        # - Other instances (such as Linux): The hostname must be **2** to **64** characters in length. Multiple periods (.) are supported. Each segment separated by a period can contain uppercase letters, lowercase letters, digits, and hyphens (-).
        self.host_name = host_name
        # The ID of the image that is used to start the instance.
        self.image_id = image_id
        # The name of the instance. Naming conventions:
        # 
        # - The name must be **2** to **128** characters in length and can contain letters and Chinese characters.
        # - The name must start with an uppercase letter, a lowercase letter, or a Chinese character. It cannot start with http:// or https://.
        # - The name can contain digits, colons (:), underscores (_), periods (.), or hyphens (-).
        # 
        # If this parameter is not specified, the default value is the InstanceId of the instance.
        self.instance_name = instance_name
        # The instance type.
        # 
        # For details about instance types, see [Limits](https://help.aliyun.com/document_detail/66124.html).
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # This parameter is required when you create an instance for the first time. If you already have instance resources, the existing billing method is used by default. Valid values:
        # 
        # - **BandwidthByDay**: daily peak bandwidth.
        # 
        # - **95BandwidthByMonth**: monthly 95th percentile bandwidth.
        self.internet_charge_type = internet_charge_type
        # The IP type. Valid values:
        # 
        # - **ipv4** (default): IPv4.
        # 
        # - **ipv6**: IPv6.
        # 
        # - **ipv4Andipv6**: IPv4 and IPv6.
        self.ip_type = ip_type
        # The name of the key pair. Only a single name is supported.
        self.key_pair_name = key_pair_name
        self.owner_id = owner_id
        # The password of the instance.
        # 
        # The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ```()`~!@#$%^&*-_+=|{}[]:;\\"<>,.?/```
        self.password = password
        # Specifies whether to use the preset password of the image. Valid values:
        # 
        # - **true**: The preset password of the image is used. The **Password** parameter must be empty, and you must make sure that the image has a preset password.
        # - **false**: The preset password of the image is not used.
        self.password_inherit = password_inherit
        # The payment method. Currently, this is a fixed value of Subscription (subscription instance). Modification is not supported.
        self.payment_type = payment_type
        # The subscription duration. Valid values: **1** to **9** and **12**. Unit: months.
        # 
        # This parameter is required.
        self.period = period
        # The private IP address. If you specify a private IP address, you must also specify the VSwitchId parameter. The vSwitch must be created in advance. Otherwise, an error is returned.
        self.private_ip_address = private_ip_address
        # Specifies whether a public IP address can be assigned to the specified instance. Valid values:
        # 
        # - **true** (default): A public IP address can be assigned.
        # - **false**: A public IP address cannot be assigned.
        self.public_ip_identification = public_ip_identification
        # The number of instances.
        # 
        # This parameter is required.
        self.quantity = quantity
        # Specifies whether to add sequential suffixes to **HostName** and **InstanceName**. The sequential suffixes start from **001** and cannot exceed **999**.
        # 
        # Example: **LocalHost001**, **LocalHost002**, **MyInstance001**, and **MyInstance002**.
        # 
        # Default value: **false**.
        self.unique_suffix = unique_suffix
        # The custom data. The data must start with `#!`. The maximum length is 256 characters and the maximum size is 16 KB. Only custom data scripts are supported. InstanceMetaData rendering is not supported.
        # 
        # 
        # You can pass in custom data that is Base64-encoded. When you call the API to initiate a request, the custom data you specify is not encrypted. Do not pass in confidential information such as passwords and private keys in plaintext. If you need to pass in passwords or private keys, encrypt the content first and then Base64-encode it before passing it in. Decrypt the content in the same way inside the instance.
        # 
        # For more information, see [Data format](https://cloudinit.readthedocs.io/en/latest/topics/format.html).
        self.user_data = user_data
        # The vSwitch ID.
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
        # The size of the system cloud disk. Unit: GiB. The value must be a multiple of 10 and cannot be smaller than the image size. For the valid range, refer to the SystemDiskMinSize and SystemDiskMaxSize values returned by DescribeAvailableResourceInfo. 20 GiB and 40 GiB are common configurations and do not indicate that only these two values are supported.
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
        # The size of the first data cloud disk. Unit: GiB. The size must be at least 20 GiB and a multiple of 10.
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

