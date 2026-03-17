# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySagWifiRequest(DaraModel):
    def __init__(
        self,
        authentication_type: str = None,
        bandwidth: str = None,
        channel: str = None,
        encrypt_algorithm: str = None,
        is_auth: str = None,
        is_broadcast: str = None,
        is_enable: str = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        ssid: str = None,
        smart_agid: str = None,
        smart_agsn: str = None,
    ):
        # The authentication type. Valid values:
        # 
        # *   **NONE**
        # *   **WPA-PSK**
        # *   **WPA2-PSK**
        self.authentication_type = authentication_type
        # The bandwidth of the channel. Valid values:
        # 
        # *   **Automatic**
        # *   **20 MHz**
        # *   **40 MHz**
        self.bandwidth = bandwidth
        # The Wi-Fi channel.
        # 
        # Valid values: **0 to 11**.
        self.channel = channel
        # The encryption algorithm. Valid values:
        # 
        # *   **AUTO**: automatically selects the encryption algorithm.
        # *   **TKIP**: uses the Temporal Key Integrity Protocol (TKIP).
        # *   **AES**: uses the Advanced Encryption Standard authorized by Wi-Fi®.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether wireless security is enabled. Valid values:
        # 
        # *   **true**: enables wireless security.
        # *   **False**: disables wireless security.
        self.is_auth = is_auth
        # Specifies whether broadcast over Wi-Fi is enabled. Valid values:
        # 
        # *   **true**: enables broadcast.
        # *   **False**: disables broadcast.
        # 
        # >  Only after you enable broadcast, terminals that support wireless connections can search the Wi-Fi network by its SSID and receive Wi-Fi signals.
        self.is_broadcast = is_broadcast
        # Specifies whether Wi-Fi is enabled. Valid values:
        # 
        # *   **true**: enables Wi-Fi.
        # *   **False**: disables Wi-Fi.
        # 
        # This parameter is required.
        self.is_enable = is_enable
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password used to connect to the Wi-Fi network.
        # 
        # The password must be 8 to 32 characters in length, and can contain digits and letters.
        self.password = password
        # The ID of the region where the SAG instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The service set identifier (SSID) of the Wi-Fi network.
        # 
        # The name must be 1 to 31 characters in length, and can contain digits and letters.
        self.ssid = ssid
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The serial number of the SAG device.
        # 
        # This parameter is required.
        self.smart_agsn = smart_agsn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_type is not None:
            result['AuthenticationType'] = self.authentication_type

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm

        if self.is_auth is not None:
            result['IsAuth'] = self.is_auth

        if self.is_broadcast is not None:
            result['IsBroadcast'] = self.is_broadcast

        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.ssid is not None:
            result['SSID'] = self.ssid

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.smart_agsn is not None:
            result['SmartAGSn'] = self.smart_agsn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationType') is not None:
            self.authentication_type = m.get('AuthenticationType')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')

        if m.get('IsAuth') is not None:
            self.is_auth = m.get('IsAuth')

        if m.get('IsBroadcast') is not None:
            self.is_broadcast = m.get('IsBroadcast')

        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SSID') is not None:
            self.ssid = m.get('SSID')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SmartAGSn') is not None:
            self.smart_agsn = m.get('SmartAGSn')

        return self

