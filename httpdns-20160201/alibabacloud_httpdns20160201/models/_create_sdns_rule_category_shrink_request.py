# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSdnsRuleCategoryShrinkRequest(DaraModel):
    def __init__(
        self,
        client_ip_ranges_shrink: str = None,
        domain_name: str = None,
        enable: bool = None,
        line_id: str = None,
        match_type: str = None,
        paths_shrink: str = None,
        rules_shrink: str = None,
    ):
        # The array of client IP address ranges required for the IP_RANGE pattern. Send this parameter as a JSON form field. Do not specify this parameter for the LINE pattern. This parameter supports single IPv4 and IPv6 addresses, CIDR blocks, and start-end ranges. Multiple entries have an OR relationship. For CIDR blocks, the IPv4 prefix length ranges from 0 to 32, and the IPv6 prefix length ranges from 0 to 128. Start-end ranges are inclusive and must belong to the same address family, and the start address cannot be greater than the end address. Duplicates, inclusions, and overlaps are allowed within the same policy. When the policy is saved and read back, the array sequence, duplicates, and original text of each string are preserved. The array can contain up to 2,000 array elements. The total number of parsed non-empty address expressions ranges from 1 to 2,000, and duplicates are counted. We recommend that you specify one expression per array element. It is compatible with line breaks within an array element. Each expression can contain up to 128 characters, including leading and trailing spaces. The serialized UTF-8 JSON content cannot exceed 65,535 bytes. The quantity and byte limits take effect simultaneously. Overlaps are not allowed between different IP_RANGE policies for the same account, domain name, and address family. Disabled policies are also checked. Disabling a policy does not release the ranges. This limit does not compare independent configurations of LINE policies and the legacy SetIPRegionResult operation.
        self.client_ip_ranges_shrink = client_ip_ranges_shrink
        # The domain name connected to HTTPDNS for the current account. This parameter is required.
        self.domain_name = domain_name
        # Specifies whether to enable the policy upon creation. If this parameter is omitted or set to false, the policy is disabled (Status=0). If this parameter is set to true, the policy is enabled (Status=1), and you do not need to call the enable operation. This parameter applies to the LINE and IP_RANGE modes. Actual resolution still requires waiting for configuration propagation.
        self.enable = enable
        # The line identifier required for the LINE mode. Valid values:
        # - internal: the Chinese mainland.
        # - overseas: outside the Chinese mainland.
        # 
        # Do not specify this parameter for the IP_RANGE mode.
        self.line_id = line_id
        # The match type. Valid values:
        # - LINE: the line mode.
        # - IP_RANGE: the client IP address range mode.
        # 
        # If this parameter is omitted, it is processed as LINE. To create an IP address range policy, you must explicitly set this parameter to IP_RANGE and provide ClientIpRanges. You cannot provide LineId or Paths at the same time. The match type cannot be changed after creation.
        self.match_type = match_type
        # The line selection path that describes the line conditions at each level. This parameter applies only to the LINE mode. The IP_RANGE mode does not use line paths. When you create a line policy, provide valid options at each level. Use x for the default option. For the Chinese mainland, the levels include ISP, region, and province. For regions outside the Chinese mainland, the levels include continent and region.
        self.paths_shrink = paths_shrink
        # The complete list of rules. This parameter is required and must contain at least one rule. When matching only by IP address range, configure a default rule without ArgKeys and Args, and configure the A or AAAA destination addresses in the Records of this rule. When saved, the serialized UTF-8 JSON content must be less than 65,535 bytes.
        self.rules_shrink = rules_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip_ranges_shrink is not None:
            result['ClientIpRanges'] = self.client_ip_ranges_shrink

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.line_id is not None:
            result['LineId'] = self.line_id

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.paths_shrink is not None:
            result['Paths'] = self.paths_shrink

        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIpRanges') is not None:
            self.client_ip_ranges_shrink = m.get('ClientIpRanges')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Paths') is not None:
            self.paths_shrink = m.get('Paths')

        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')

        return self

