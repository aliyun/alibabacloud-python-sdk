# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SdnsVerifyRuleCategoryShrinkRequest(DaraModel):
    def __init__(
        self,
        args_shrink: str = None,
        cip: str = None,
        client_ip_ranges_shrink: str = None,
        match_type: str = None,
        rules_shrink: str = None,
    ):
        # The parameter object used for the current validation. If no custom parameters are used, pass an empty JSON object {}. Do not pass an empty string or null.
        self.args_shrink = args_shrink
        # The simulated client IP address. This parameter is required in IP_RANGE mode. Supports a single IPv4 or IPv6 address. CIDR blocks and start-to-end ranges are not supported. This parameter is used for CIDR block matching in the current request and does not change the source of the actual DNS resolution request.
        self.cip = cip
        # The array of client CIDR blocks that must be provided in the IP_RANGE pattern. Send this parameter as a JSON form field. Do not pass this parameter in the LINE pattern. Supports single IPv4 and IPv6 addresses, CIDR blocks, and start-to-end ranges. Multiple entries have an OR relationship. For CIDR blocks, the IPv4 prefix length ranges from 0 to 32, and the IPv6 prefix length ranges from 0 to 128. Start-to-end ranges are inclusive and must belong to the same address family, with the start address not greater than the end address. Overlapping, containing, and duplicate ranges are allowed within the same policy. When the policy is saved and read back, the array sequence, duplicate items, and the original text of each string are preserved. The array can contain up to 2,000 array elements. The total number of parsed non-empty address expressions ranges from 1 to 2,000, including duplicates. Specify one expression per array element. It is compatible with line breaks within an array element. Each expression can contain up to 128 characters, including leading and trailing whitespace. The serialized UTF-8 JSON content cannot exceed 65,535 bytes. Both the quantity and byte limits apply simultaneously. To authenticate, the system only checks the ranges that you commit and does not check for conflicts with saved policies.
        self.client_ip_ranges_shrink = client_ip_ranges_shrink
        # The match type. Valid values:
        # - LINE: line mode
        # - IP_RANGE: client CIDR block mode
        # If this parameter is omitted, LINE is used. In IP_RANGE mode, you must provide both ClientIpRanges and Cip.
        self.match_type = match_type
        # The complete list of rules. This parameter is required and must contain at least one rule. If you only need to match CIDR blocks, configure a default rule without ArgKeys and Args, and configure the A/AAAA destination addresses in the Records field of this rule. This operation is used for match validation and does not save the rules.
        self.rules_shrink = rules_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args_shrink is not None:
            result['Args'] = self.args_shrink

        if self.cip is not None:
            result['Cip'] = self.cip

        if self.client_ip_ranges_shrink is not None:
            result['ClientIpRanges'] = self.client_ip_ranges_shrink

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args_shrink = m.get('Args')

        if m.get('Cip') is not None:
            self.cip = m.get('Cip')

        if m.get('ClientIpRanges') is not None:
            self.client_ip_ranges_shrink = m.get('ClientIpRanges')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')

        return self

