# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyOperateVulRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        from_: str = None,
        info: str = None,
        operate_type: str = None,
        reason: str = None,
        resource_directory_account_id: int = None,
        type: str = None,
    ):
        # The client token used to ensure request idempotence. Use a different token for each request. Only ASCII characters are supported. The value can be up to 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform only a dry run for this request. Valid values: true: performs only a dry run without executing the actual operation. false: sends the request normally. Default value: false.
        self.dry_run = dry_run
        # The source identifier of the request. Set this parameter to **sas**.
        self.from_ = from_
        # The information about the vulnerability to handle. This parameter is in JSON format and contains the following fields:
        # 
        # - **name**: The name of the vulnerability.
        # - **uuid**: The UUID of the server that has the vulnerability.
        # - **tag**: The label of the vulnerability. Valid values:
        #     - **oval**: Linux software vulnerability
        #     - **system**: Windows system vulnerability
        #     - **cms**: Web-CMS vulnerability
        # 
        # > For other vulnerability types, call the [DescribeVulList](~~DescribeVulList~~) operation to obtain vulnerability information.
        # 
        # - **isFront**: Specifies whether the Windows patch is a prerequisite patch. Set this parameter only when handling Windows system vulnerabilities. You can ignore this parameter for other vulnerability types. Valid values:
        #     - **0**: No.
        #     - **1**: Yes.
        # 
        # > Batch processing is supported. Separate multiple vulnerability entries with commas (,). Call the [DescribeVulList](~~DescribeVulList~~) operation to obtain vulnerability information.
        # 
        # This parameter is required.
        self.info = info
        # The operation to perform on the vulnerability. Valid values:
        # - **vul_fix**: Fix the vulnerability.
        # - **vul_verify**: Verify the vulnerability.
        # - **vul_ignore**: Ignore the vulnerability.
        # - **vul_undo_ignore**: Cancel ignoring the vulnerability.
        # - **vul_delete**: Delete the vulnerability.
        # 
        # This parameter is required.
        self.operate_type = operate_type
        # The reason for ignoring the vulnerability. This parameter is required only when the operation is set to **ignore** (that is, **OperateType** is set to **vul_ignore**).
        self.reason = reason
        # The ID of the Alibaba Cloud account associated with a member account in the resource directory.
        # >Call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The type of vulnerability to handle. Valid values:
        # - **cve**: Linux software vulnerability
        # - **sys**: Windows system vulnerability
        # - **cms**: Web-CMS vulnerability
        # - **emg**: Emergency vulnerability
        # - **app**: Application vulnerability
        # - **sca**: Software constituency parsing vulnerability
        # 
        # > Fix operations are not supported for emergency vulnerabilities (emg), application vulnerabilities (app), or software constituency parsing vulnerabilities (sca). These vulnerability types do not support the execute vulnerability fix operation.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.from_ is not None:
            result['From'] = self.from_

        if self.info is not None:
            result['Info'] = self.info

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

