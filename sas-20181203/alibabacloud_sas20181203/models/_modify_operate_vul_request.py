# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyOperateVulRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        from_: str = None,
        info: str = None,
        operate_type: str = None,
        reason: str = None,
        resource_directory_account_id: int = None,
        type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. Use a different token for each request. The token supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The source identifier of the request. Set the value to **sas**.
        self.from_ = from_
        # The information about the vulnerability to handle. This parameter is in JSON format and contains the following fields:
        # 
        # - **name**: The name of the vulnerability.
        # - **uuid**: The UUID of the server on which the vulnerability is detected.
        # - **tag**: The tag of the vulnerability. Valid values:
        #     - **oval**: Linux software vulnerability.
        #     - **system**: Windows system vulnerability.
        #     - **cms**: Web-CMS vulnerability.
        # 
        # > For other vulnerability types, call the [DescribeVulList](~~DescribeVulList~~) operation to obtain vulnerability information.
        # 
        # - **isFront**: Specifies whether the Windows patch is a prerequisite patch. This parameter is required only when you handle Windows system vulnerabilities. You can ignore this parameter for other vulnerability types. Valid values:
        #     - **0**: No.
        #     - **1**: Yes.
        # 
        # > Batch processing of vulnerabilities is supported. Separate multiple vulnerability entries with commas (,). Call the [DescribeVulList](~~DescribeVulList~~) operation to obtain vulnerability information.
        # 
        # This parameter is required.
        self.info = info
        # The operation to perform on the vulnerability. Valid values:
        # - **vul_fix**: fixes the vulnerability.
        # - **vul_verify**: verifies the vulnerability.
        # - **vul_ignore**: ignores the vulnerability.
        # - **vul_undo_ignore**: cancels ignoring the vulnerability.
        # - **vul_delete**: deletes the vulnerability.
        # 
        # This parameter is required.
        self.operate_type = operate_type
        # The reason for ignoring the vulnerability.
        # > This parameter is required only when the operation type is **ignore** (OperateType is set to **vul_ignore**).
        self.reason = reason
        self.resource_directory_account_id = resource_directory_account_id
        # The type of the vulnerability to handle. Valid values:
        # - **cve**: Linux software vulnerability.
        # - **sys**: Windows system vulnerability.
        # - **cms**: Web-CMS vulnerability.
        # - **emg**: emergency vulnerability.
        # - **app**: application vulnerability.
        # - **sca**: software constituency parsing vulnerability.
        # 
        # > Emergency vulnerabilities (emg), application vulnerabilities (app), and software constituency parsing vulnerabilities (sca) do not support the execute vulnerability fix operation.
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

