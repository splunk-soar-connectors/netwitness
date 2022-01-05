[comment]: # "Auto-generated SOAR connector documentation"
# NetWitness Logs and Packets

Publisher: Splunk  
Connector Version: 2\.1\.1  
Product Vendor: RSA  
Product Name: NetWitness Logs and Packets  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.0\.0  

This app supports investigative actions to collect log and packet captures from RSA NetWitness Logs and Packets

[comment]: # " File: readme.md"
[comment]: # "  "
[comment]: # "  Copyright (c) 2017-2022 Splunk Inc."
[comment]: # ""
[comment]: # "  Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "  you may not use this file except in compliance with the License."
[comment]: # ""
[comment]: # "  You may obtain a copy of the License at  "
[comment]: # "      http://www.apache.org/licenses/LICENSE-2.0   "
[comment]: # "  "
[comment]: # "  Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "  the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "  either express or implied. See the License for the specific language governing permissions"
[comment]: # "  and limitations under the License."
[comment]: # ""
The app uses HTTP/ HTTPS protocol for communicating with the Netwitness server. Below are the
default ports used by Splunk SOAR.

|         Service Name | Transport Protocol | Port |
|----------------------|--------------------|------|
|         http         | tcp                | 80   |
|         https        | tcp                | 443  |


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a NetWitness Logs and Packets asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**url** |  required  | string | URL
**verify\_server\_cert** |  optional  | boolean | Verify server certificate
**username** |  required  | string | Username
**password** |  required  | password | Password

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the credentials provided for connectivity  
[get pcap](#action-get-pcap) - Download a packet capture file from Netwitness Logs and Packets and add it to the vault  
[get log](#action-get-log) - Download a log capture file from Netwitness Logs and Packets and add it to the vault  
[upload file](#action-upload-file) - Upload a feed or parser file to a NetWitness Decoder  
[restart device](#action-restart-device) - Restart the configured device  

## action: 'test connectivity'
Validate the credentials provided for connectivity

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'get pcap'
Download a packet capture file from Netwitness Logs and Packets and add it to the vault

Type: **investigate**  
Read only: **True**

There are several ways to search NetWitness Logs and Packets to get capture files\:<ul><li>By session ID, which can be done in three ways\:<ul><li>Searching by a single session ID\. The downloaded capture file would have the name <b>netwitness\-&lt;id&gt;</b>\.</li><li>Searching by a list of session IDs\. In this case the <b>session\_ids</b> parameter should be a comma separated list\. The downloaded capture file would have the name <b>netwitness\-&lt;id1\_id2\_id3\.\.\.&gt;</b>\. The session ID list will be cut off at 50 characters\.</li><li>Searching by a range of session IDs\. In this case the <b>session\_ids</b> parameter would have the format <b>start\_id\-end\_id</b>\. The downloaded capture file would have the name <b>netwitness\-&lt;start\_id&gt;\-&lt;end\_id&gt;</b>\. NOTE\: Including spaces when specifying a range of sessions IDs will cause the action to fail\.</li></ul></li><li>By query\. The <b>query</b> parameter should be treated as the <b>where</b> clause of a database query using the meta keys configured on the NetWitness server\. The downloaded capture file would have the name <b>netwitness\-&lt;random\_uuid&gt;</b>\. Some example queries\:<ul><li>ip\.src=10\.10\.10\.10</li><li>ip\.dst=10\.10\.0\.1 \|\| ip\.dst=10\.10\.0\.2</li><li>ip\.src=10\.10\.0\.7 && ip\.dst=10\.10\.0\.8</li><li>ip\.src exists</li></ul></li><li>By time frame, which requires both the <b>start\_time</b> and <b>end\_time</b> parameters be given\. The downloaded capture file would have the name <b>netwitness\-&lt;start\_time&gt;\_&lt;end\_time&gt;</b>\.</li></ul>NOTE\: If <b>start\_time</b> and <b>end\_time</b> are included along with a <b>query</b>, then the time\-frame will be appended to the end of the query\. For example\: if the query is ip\.src=10\.10\.10\.10, the start time is 2018\-01\-01 00\:00\:00, and the end time is 2018\-01\-01 23\:59\:59, then the final query would be ip\.src=10\.10\.0\.7 && time=&quot;2018\-01\-01 00\:00\:00&quot;\-&quot;2018\-01\-01 23\:59\:59&quot;<br><br><b>file\_name</b> is an optional parameter that, if specified, will result in the capture file being given that name\. It will override the filenames mentioned above\. The appropriate extension, <b>\.pcap</b> \(or <b>\.json</b> for <b>get log</b>\), will be appended to the file name if it is not already present\.<br><br>If a query returns no data, the action will pass, but no file will be added to the vault\. Queries to decoders that return large amounts of data, which take more than five minutes, can time out, in which case the action will fail\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**session\_ids** |  optional  | Session IDs in a list \(72,637,1298\.\.\.\), as a range \(0\-9999\), or singly \(485\) | string |  `netwitness session ids` 
**query** |  optional  | A where query using configured meta keys | string | 
**start\_time** |  optional  | Start time in UTC \(YYYY\-MM\-DD HH\:MM\:SS\) | string | 
**end\_time** |  optional  | End time in UTC \(YYYY\-MM\-DD HH\:MM\:SS\) | string | 
**file\_name** |  optional  | File name to give the downloaded capture | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.end\_time | string | 
action\_result\.parameter\.file\_name | string | 
action\_result\.parameter\.query | string | 
action\_result\.parameter\.session\_ids | string |  `netwitness session ids` 
action\_result\.parameter\.start\_time | string | 
action\_result\.data\.\*\.file\_name | string |  `file name` 
action\_result\.data\.\*\.size | numeric | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.vault\_id | string |  `vault id` 
action\_result\.summary\.file\_availability | boolean | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get log'
Download a log capture file from Netwitness Logs and Packets and add it to the vault

Type: **investigate**  
Read only: **True**

See <b>get pcap</b> for further information on this action\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**session\_ids** |  optional  | Session IDs in a list \(72,637,1298\.\.\.\), as a range \(0\-9999\), or singly \(485\) | string |  `netwitness session ids` 
**query** |  optional  | A where query using configured meta keys | string | 
**start\_time** |  optional  | Start time in UTC \(YYYY\-MM\-DD HH\:MM\:SS\) | string | 
**end\_time** |  optional  | End time in UTC \(YYYY\-MM\-DD HH\:MM\:SS\) | string | 
**file\_name** |  optional  | File name to give the downloaded capture | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.end\_time | string | 
action\_result\.parameter\.file\_name | string | 
action\_result\.parameter\.query | string | 
action\_result\.parameter\.session\_ids | string |  `netwitness session ids` 
action\_result\.parameter\.start\_time | string | 
action\_result\.data\.\*\.file\_name | string |  `file name` 
action\_result\.data\.\*\.size | numeric | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.vault\_id | string |  `vault id` 
action\_result\.summary\.file\_availability | boolean | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'upload file'
Upload a feed or parser file to a NetWitness Decoder

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**vault\_id** |  required  | Vault ID of parser/feed to upload | string |  `vault id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.vault\_id | string |  `vault id` 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'restart device'
Restart the configured device

Type: **generic**  
Read only: **False**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 