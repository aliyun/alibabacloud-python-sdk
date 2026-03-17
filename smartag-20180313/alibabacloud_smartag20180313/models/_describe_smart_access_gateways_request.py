# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSmartAccessGatewaysRequest(DaraModel):
    def __init__(
        self,
        acl_ids: str = None,
        associated_ccn_id: str = None,
        associated_ccn_name: str = None,
        business_state: str = None,
        can_associate_qos: bool = None,
        hardware_type: str = None,
        instance_type: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        serial_number: str = None,
        smart_agid: str = None,
        smart_agids: List[str] = None,
        software_version: str = None,
        status: str = None,
        unbound_acl_ids: str = None,
        version_comparator: str = None,
    ):
        # The ID of the ACL with which the SAG instance is associated.
        self.acl_ids = acl_ids
        # The ID of the CCN instance with which the SAG instance is associated.
        self.associated_ccn_id = associated_ccn_id
        # The name of the associated CCN instance.
        # 
        # The name must be 2 to 100 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        self.associated_ccn_name = associated_ccn_name
        # The business status of the SAG instance. Valid values:
        # 
        # *   **Normal**: running as expected.
        # *   **Arrearage**: locked due to overdue payments.
        self.business_state = business_state
        # Specifies whether the SAG instance can be associated with a quality of service (QoS) policy. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # Specifies whether to query SAG instances that cannot be associated with QoS policies.
        self.can_associate_qos = can_associate_qos
        # The model of SAG device. Valid values:
        # 
        # *   **sag-1000**
        # *   **sag-100wm**
        self.hardware_type = hardware_type
        # The type of the SAG instance. Valid values:
        # 
        # *   **software**: an SAG app instance
        # *   **hardware**: an SAG CPE instance
        self.instance_type = instance_type
        # The name of the SAG instance.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **10**. Valid values: **1** to **50**.
        self.page_size = page_size
        # The ID of the region where the SAG instance is deployed.
        self.region_id = region_id
        # The ID of the resource group to which the SAG instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The serial number of the SAG device.
        self.serial_number = serial_number
        # The ID of the SAG instance.
        self.smart_agid = smart_agid
        # The IDs of the SAG instances.
        self.smart_agids = smart_agids
        # The software version of the SAG device.
        self.software_version = software_version
        # The status of the SAG instance. Valid values:
        # 
        # *   **Ordered**: Your order has been placed.
        # *   **Delivered**: Your order has been shipped.
        # *   **Received**: You have received the SAG device.
        # *   **Returning**: The order is being returned.
        # *   **Active**: The SAG device is active.
        # *   **init**: The SAG device is being initialized.
        # *   **Offline**: The SAG device is disconnected.
        self.status = status
        # The ID of the ACL rule.
        # 
        # Specifies that the SAG instance which is not associated with the ACL is queried. Separate ACL IDs with commas (,).
        self.unbound_acl_ids = unbound_acl_ids
        # The version filter. Valid values:
        # 
        # *   **greater**: later than the current version
        # *   **less**: earlier than the current version
        # *   **equals**: equal to the current version
        self.version_comparator = version_comparator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids

        if self.associated_ccn_id is not None:
            result['AssociatedCcnId'] = self.associated_ccn_id

        if self.associated_ccn_name is not None:
            result['AssociatedCcnName'] = self.associated_ccn_name

        if self.business_state is not None:
            result['BusinessState'] = self.business_state

        if self.can_associate_qos is not None:
            result['CanAssociateQos'] = self.can_associate_qos

        if self.hardware_type is not None:
            result['HardwareType'] = self.hardware_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.smart_agids is not None:
            result['SmartAGIds'] = self.smart_agids

        if self.software_version is not None:
            result['SoftwareVersion'] = self.software_version

        if self.status is not None:
            result['Status'] = self.status

        if self.unbound_acl_ids is not None:
            result['UnboundAclIds'] = self.unbound_acl_ids

        if self.version_comparator is not None:
            result['VersionComparator'] = self.version_comparator

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')

        if m.get('AssociatedCcnId') is not None:
            self.associated_ccn_id = m.get('AssociatedCcnId')

        if m.get('AssociatedCcnName') is not None:
            self.associated_ccn_name = m.get('AssociatedCcnName')

        if m.get('BusinessState') is not None:
            self.business_state = m.get('BusinessState')

        if m.get('CanAssociateQos') is not None:
            self.can_associate_qos = m.get('CanAssociateQos')

        if m.get('HardwareType') is not None:
            self.hardware_type = m.get('HardwareType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SmartAGIds') is not None:
            self.smart_agids = m.get('SmartAGIds')

        if m.get('SoftwareVersion') is not None:
            self.software_version = m.get('SoftwareVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnboundAclIds') is not None:
            self.unbound_acl_ids = m.get('UnboundAclIds')

        if m.get('VersionComparator') is not None:
            self.version_comparator = m.get('VersionComparator')

        return self

