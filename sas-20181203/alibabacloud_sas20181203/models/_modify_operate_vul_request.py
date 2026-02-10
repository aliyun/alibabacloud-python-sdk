# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyOperateVulRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        info: str = None,
        operate_type: str = None,
        reason: str = None,
        type: str = None,
    ):
        # The request ID. Set the value to **sas**.
        self.from_ = from_
        # The details of the vulnerability. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **name**: the name of the vulnerability.
        # 
        # *   **uuid**: the UUID of the server on which the vulnerability is detected.
        # 
        # *   **tag**: the tag that is added to the vulnerability. Valid values:
        # 
        #     *   **oval**: Linux software vulnerability
        #     *   **system**: Windows system vulnerability
        #     *   **cms**: Web-CMS vulnerability
        # 
        # >  You can call the [DescribeVulList](~~DescribeVulList~~) operation to query the tags that are added to vulnerabilities of other types.
        # 
        # *   **isFront**: specifies whether a pre-patch is required to fix the Windows system vulnerability. This field is required only for Windows system vulnerabilities. Valid values:
        # 
        #     *   **0**: no
        #     *   **1**: yes
        # 
        # >  You can fix multiple vulnerabilities at a time. Separate the details of multiple vulnerabilities with commas (,). You can call the [DescribeVulLIst](~~DescribeVulList~~) operation to query the details of vulnerabilities.
        # 
        # This parameter is required.
        self.info = info
        # The operation that you want to perform on the vulnerability. Valid values:
        # 
        # *   **vul_fix**: fixes the vulnerability.
        # *   **vul_verify**: verifies the vulnerability fix.
        # *   **vul_ignore**: ignores the vulnerability.
        # *   **vul_undo_ignore**: cancels ignoring the vulnerability.
        # *   **vul_delete**: deletes the vulnerability.
        # 
        # This parameter is required.
        self.operate_type = operate_type
        # The reason why the vulnerability is **ignored**.
        # 
        # >  This parameter is required only when you set **OperateType** to **vul_ignore**.
        self.reason = reason
        # The type of the vulnerability. Valid values:
        # 
        # *   **cve**: Linux software vulnerability
        # *   **sys**: Windows system vulnerability
        # *   **cms**: Web-CMS vulnerability
        # *   **emg**: urgent vulnerability
        # *   **app**: application vulnerability
        # *   **sca**: vulnerability that is detected based on software component analysis
        # 
        # >  You cannot fix the urgent vulnerabilities, application vulnerabilities, or vulnerabilities that are detected based on software component analysis.
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
        if self.from_ is not None:
            result['From'] = self.from_

        if self.info is not None:
            result['Info'] = self.info

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

