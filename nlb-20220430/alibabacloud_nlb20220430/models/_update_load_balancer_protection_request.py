# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLoadBalancerProtectionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        deletion_protection_enabled: bool = None,
        deletion_protection_reason: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        modification_protection_reason: str = None,
        modification_protection_status: str = None,
        region_id: str = None,
    ):
        # The client token used to ensure the idempotence of the request.
        # 
        # You can use the client to generate this value. Ensure that the value is unique among all requests. Only ASCII characters are allowed.
        # 
        # >  If you do not specify this parameter, the value of **RequestId** is used.**** **RequestId** of each request is different.
        self.client_token = client_token
        # Specifies whether to enable deletion protection. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.deletion_protection_enabled = deletion_protection_enabled
        # The reason why deletion protection is enabled. The reason must be 2 to 128 characters in length, can contain letters, digits, periods (.), underscores (_), and hyphens (-), and must start with a letter.
        # 
        # >  This parameter takes effect only when **DeletionProtectionEnabled** is set to **true**.
        self.deletion_protection_reason = deletion_protection_reason
        # Specifies whether to perform a dry run, without sending the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends a request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the NLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The reason why the configuration read-only mode is enabled. The reason must be 2 to 128 characters in length, can contain letters, digits, periods (.), underscores (_), and hyphens (-), and must start with a letter.
        # 
        # >  This parameter takes effect only when **Status** is set to **ConsoleProtection**.
        self.modification_protection_reason = modification_protection_reason
        # Specifies whether to enable the configuration read-only mode. Valid values:
        # 
        # *   **NonProtection**: disables the configuration read-only mode. In this case, you cannot set the **ModificationProtectionReason** parameter. If you specify **ModificationProtectionReason**, the value is cleared.
        # *   **ConsoleProtection**: enables the configuration read-only mode. In this case, you can specify **ModificationProtectionReason**.
        # 
        # >  If you set this parameter to **ConsoleProtection**, you cannot use the NLB console to modify configurations of the NLB instance. However, you can call API operations to modify the instance configurations.
        self.modification_protection_status = modification_protection_status
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.deletion_protection_enabled is not None:
            result['DeletionProtectionEnabled'] = self.deletion_protection_enabled

        if self.deletion_protection_reason is not None:
            result['DeletionProtectionReason'] = self.deletion_protection_reason

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.modification_protection_reason is not None:
            result['ModificationProtectionReason'] = self.modification_protection_reason

        if self.modification_protection_status is not None:
            result['ModificationProtectionStatus'] = self.modification_protection_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeletionProtectionEnabled') is not None:
            self.deletion_protection_enabled = m.get('DeletionProtectionEnabled')

        if m.get('DeletionProtectionReason') is not None:
            self.deletion_protection_reason = m.get('DeletionProtectionReason')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('ModificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('ModificationProtectionReason')

        if m.get('ModificationProtectionStatus') is not None:
            self.modification_protection_status = m.get('ModificationProtectionStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

