def define_observable_hash_type(h_type):
    if 'sha' in h_type:
        return 'SHA-{}'.format(h_type.split('sha')[1])
    if h_type == 'md5':
        return h_type.upper()
    return h_type

def parse_name(observable, _):
    return observable['0'].get('name')

def parse_value(observable, _):
    return observable['0'].get('value')

def parse_attachment(observable, _):
    return observable['0'].get('payload_bin')

def parse_domain_ip(observable, _):
    return "{}|{}".format(parse_value(observable, _), observable['1'].get('value'))

def parse_email_message(observable, attribute_type):
    return observable['0'].get(attribute_type.split('-')[1])

def parse_hash(observable, attribute_type):
    observable_type = define_observable_hash_type(attribute_type)
    return observable['0']['hashes'].get(observable_type)

def parse_ip_port(observable, _):
    try:
        port = observable['1']['src_port']
    except:
        port = observable['1']['dst_port']
    return '{}|{}'.format(parse_value(observable, _), port)

def parse_hostname_port(observable, _):
    return '{}|{}'.format(parse_value(observable, _), observable['1'].get('dst_port'))

def parse_filename_hash(observable, attribute_type):
    _, h = attribute_type.split('|')
    return "{}|{}".format(parse_name(observable, _), parse_hash(observable, h))

def parse_malware_sample(observable, _):
    return parse_filename_hash(observable, 'filename|md5')

def parse_port(observable, _):
    return observable

def parse_regkey(observable, _):
    return observable['0'].get('key')

def parse_regkey_value(observable, _):
    return '{}|{}'.format(parse_regkey(observable,_), parse_name(observable, _))

misp_types_mapping = {
    'md5': parse_hash,
    'sha1': parse_hash,
    'sha256': parse_hash,
    'filename': parse_name,
    'filename|md5': parse_filename_hash,
    'filename|sha1': parse_filename_hash,
    'filename|sha256': parse_filename_hash,
    'ip-src': parse_value,
    'ip-dst': parse_value,
    'hostname': parse_value,
    'domain': parse_value,
    'domain|ip': parse_domain_ip,
    'email-src': parse_value,
    'email-dst': parse_value,
    'email-subject': parse_email_message,
    'email-body': parse_email_message,
    'url': parse_value,
    'regkey': parse_regkey,
    'regkey|value': parse_regkey_value,
    'malware-sample': parse_malware_sample,
    'mutex': parse_name,
    'uri': parse_value,
    'authentihash': parse_hash,
    'ssdeep': parse_hash,
    'imphash': parse_hash,
    'pehash': parse_hash,
    'impfuzzy': parse_hash,
    'sha224': parse_hash,
    'sha384': parse_hash,
    'sha512': parse_hash,
    'sha512/224': parse_hash,
    'sha512/256': parse_hash,
    'tlsh': parse_hash,
    'filename|authentihash': parse_filename_hash,
    'filename|ssdeep': parse_filename_hash,
    'filename|imphash': parse_filename_hash,
    'filename|impfuzzy': parse_filename_hash,
    'filename|pehash': parse_filename_hash,
    'filename|sha224': parse_filename_hash,
    'filename|sha384': parse_filename_hash,
    'filename|sha512': parse_filename_hash,
    'filename|sha512/224': parse_filename_hash,
    'filename|sha512/256': parse_filename_hash,
    'filename|tlsh': parse_filename_hash,
    'x509-fingerprint-sha1': parse_hash,
    'port': parse_port,
    'ip-dst|port': parse_ip_port,
    'ip-src|port': parse_ip_port,
    'hostname|port': parse_hostname_port,
    'email-reply-to': parse_value,
    'attachment': parse_attachment,
    'mac-address': parse_value
}

cc_attribute_mapping = {'type': 'email-dst', 'relation': 'cc'}
data_attribute_mapping = {'type': 'text', 'relation': 'data'}
data_type_attribute_mapping = {'type': 'text', 'relation': 'data-type'}
domain_attribute_mapping = {'type': 'domain', 'relation': 'domain'}
dst_port_attribute_mapping = {'type': 'port', 'relation': 'dst-port'}
email_date_attribute_mapping = {'type': 'datetime', 'relation': 'send-date'}
email_subject_attribute_mapping = {'type': 'email-subject', 'relation': 'subject'}
end_datetime_attribute_mapping = {'type': 'datetime', 'relation': 'last-seen'}
filename_attribute_mapping = {'type': 'filename', 'relation': 'filename'}
ip_attribute_mapping = {'type': 'ip-dst', 'relation': 'ip'}
issuer_attribute_mapping = {'type': 'text', 'relation': 'issuer'}
key_attribute_mapping = {'type': 'regkey', 'relation': 'key'}
mime_type_attribute_mapping = {'type': 'mime-type', 'relation': 'mimetype'}
modified_attribute_mapping = {'type': 'datetime', 'relation': 'last-modified'}
regkey_name_attribute_mapping = {'type': 'text', 'relation': 'name'}
reply_to_attribute_mapping = {'type': 'email-reply-to', 'relation': 'reply-to'}
serial_number_attribute_mapping = {'type': 'text', 'relation': 'serial-number'}
size_attribute_mapping = {'type': 'size-in-bytes', 'relation': 'size-in-bytes'}
src_port_attribute_mapping = {'type': 'port', 'relation': 'src-port'}
start_datetime_attribute_mapping = {'type': 'datetime', 'relation': 'first-seen'}
to_attribute_mapping = {'type': 'email-dst', 'relation': 'to'}
url_attribute_mapping = {'type': 'url', 'relation': 'url'}
url_port_attribute_mapping = {'type': 'port', 'relation': 'port'}
x_mailer_attribute_mapping = {'type': 'email-x-mailer', 'relation': 'x-mailer'}
x509_md5_attribute_mapping = {'type': 'x509-fingerprint-md5', 'relation': 'x509-fingerprint-md5'}
x509_sha1_attribute_mapping = {'type': 'x509-fingerprint-sha1', 'relation': 'x509-fingerprint-sha1'}
x509_sha256_attribute_mapping = {'type': 'x509-fingerprint-sha256', 'relation': 'x509-fingerprint-sha256'}
x509_spka_attribute_mapping = {'type': 'text', 'relation': 'pubkey-info-algorithm'} # x509 subject public key algorithm
x509_spke_attribute_mapping = {'type': 'text', 'relation': 'pubkey-info-exponent'} # x509 subject public key exponent
x509_spkm_attribute_mapping = {'type': 'text', 'relation': 'pubkey-info-modulus'} # x509 subject public key modulus
x509_subject_attribute_mapping = {'type': 'text', 'relation': 'subject'}
x509_version_attribute_mapping = {'type': 'text', 'relation': 'version'}
x509_vna_attribute_mapping = {'type': 'datetime', 'relation': 'validity-not-after'} # x509 validity not after
x509_vnb_attribute_mapping = {'type': 'datetime', 'relation': 'validity-not-before'} # x509 validity not before

domain_ip_mapping = {'domain-name': domain_attribute_mapping,
                     'domain-name:value': domain_attribute_mapping,
                     'ipv4-addr': ip_attribute_mapping,
                     'ipv6-addr': ip_attribute_mapping,
                     'domain-name:resolves_to_refs[*].value': ip_attribute_mapping,}

email_mapping = {'date': email_date_attribute_mapping,
                 'email-message:date': email_date_attribute_mapping,
                 'to_refs': to_attribute_mapping,
                 'email-message:to_refs': to_attribute_mapping,
                 'cc_refs': cc_attribute_mapping,
                 'email-message:cc_refs': cc_attribute_mapping,
                 'subject': email_subject_attribute_mapping,
                 'email-message:subject': email_subject_attribute_mapping,
                 'X-Mailer': x_mailer_attribute_mapping,
                 'email-message:additional_header_fields.x_mailer': x_mailer_attribute_mapping,
                 'Reply-To': reply_to_attribute_mapping,
                 'email-message:additional_header_fields.reply_to': reply_to_attribute_mapping,
                 'email-message:from_ref': {'type': 'email-dst', 'relation': 'from'},
                 'email-message:body_multipart[*].body_raw_ref.name': {'type': 'email-attachment',
                                                                       'relation': 'attachment'}
                 }

file_mapping = {'mime_type': mime_type_attribute_mapping,
                'file:mime_type': mime_type_attribute_mapping,
                'name': filename_attribute_mapping,
                'file:name': filename_attribute_mapping,
                'size': size_attribute_mapping,
                'file:size': size_attribute_mapping}

ip_port_mapping = {'src_port': src_port_attribute_mapping,
                   'network-traffic:src_port': src_port_attribute_mapping,
                   'dst_port': dst_port_attribute_mapping,
                   'network-traffic:dst_port': dst_port_attribute_mapping,
                   'start': start_datetime_attribute_mapping,
                   'network-traffic:start': start_datetime_attribute_mapping,
                   'end': end_datetime_attribute_mapping,
                   'network-traffic:end': end_datetime_attribute_mapping,
                   'value': domain_attribute_mapping,
                   'domain-name:value': domain_attribute_mapping,
                   'network-traffic:dst_ref.value': ip_attribute_mapping}

regkey_mapping = {'data': data_attribute_mapping,
                  'windows-registry-key:data': data_attribute_mapping,
                  'data_type': data_type_attribute_mapping,
                  'windows-registry-key:data_type': data_type_attribute_mapping,
                  'modified': modified_attribute_mapping,
                  'windows-registry-key:modified': modified_attribute_mapping,
                  'name': regkey_name_attribute_mapping,
                  'windows-registry-key:name': regkey_name_attribute_mapping,
                  'key': key_attribute_mapping,
                  'windows-registry-key:key': key_attribute_mapping
                  }

url_mapping = {'url': url_attribute_mapping,
               'url:value': url_attribute_mapping,
               'domain-name': domain_attribute_mapping,
               'domain-name:value': domain_attribute_mapping,
               'network-traffic': url_port_attribute_mapping,
               'network-traffic:dst_port': url_port_attribute_mapping
               }

x509_mapping = {'issuer': issuer_attribute_mapping,
                'x509-certificate:issuer': issuer_attribute_mapping,
                'serial_number': serial_number_attribute_mapping,
                'x509-certificate:serial_number': serial_number_attribute_mapping,
                'subject': x509_subject_attribute_mapping,
                'x509-certificate:subject': x509_subject_attribute_mapping,
                'subject_public_key_algorithm': x509_spka_attribute_mapping,
                'x509-certificate:subject_public_key_algorithm': x509_spka_attribute_mapping,
                'subject_public_key_exponent': x509_spke_attribute_mapping,
                'x509-certificate:subject_public_key_exponent': x509_spke_attribute_mapping,
                'subject_public_key_modulus': x509_spkm_attribute_mapping,
                'x509-certificate:subject_public_key_modulus': x509_spkm_attribute_mapping,
                'validity_not_before': x509_vnb_attribute_mapping,
                'x509-certificate:validity_not_before': x509_vnb_attribute_mapping,
                'validity_not_after': x509_vna_attribute_mapping,
                'x509-certificate:validity_not_after': x509_vna_attribute_mapping,
                'version': x509_version_attribute_mapping,
                'x509-certificate:version': x509_version_attribute_mapping,
                'SHA-1': x509_sha1_attribute_mapping,
                "x509-certificate:hashes.'sha1'": x509_sha1_attribute_mapping,
                'SHA-256': x509_sha256_attribute_mapping,
                "x509-certificate:hashes.'sha256'": x509_sha256_attribute_mapping,
                'MD5': x509_md5_attribute_mapping,
                "x509-certificate:hashes.'md5'": x509_md5_attribute_mapping,
                }

def fill_observable_attributes(attributes, stix_object, object_mapping):
    for o in stix_object:
        try:
            mapping = object_mapping[o]
        except:
            continue
        attributes.append({'type': mapping.get('type'), 'object_relation': mapping.get('relation'),
                           'value': stix_object.get(o)})

def fill_pattern_attributes(pattern, object_mapping):
    attributes = []
    for p in pattern:
        p_type, p_value = p.split(' = ')
        try:
            mapping = object_mapping[p_type]
        except KeyError:
            continue
        attributes.append({'type': mapping['type'], 'object_relation': mapping['relation'],
                           'value': p_value[1:-1]})
    return attributes

def observable_domain_ip(observable):
    attributes = []
    for o in observable:
        observable_part = observable[o]
        part_type = observable_part._type
        mapping = domain_ip_mapping[part_type]
        attributes.append({'type': mapping.get('type'), 'object_relation': mapping.get('relation'),
                           'value': observable_part.get('value')})
    return attributes

def pattern_domain_ip(pattern):
    return fill_pattern_attributes(pattern, domain_ip_mapping)

def observable_email(observable):
    attributes = []
    addresses = {}
    files = {}
    for o in observable:
        observable_part = observable[o]
        part_type = observable_part._type
        if part_type == 'email-addr':
            addresses[o] = observable_part.get('value')
        elif part_type == 'file':
            files[o] = observable_part.get('name')
        else:
            message = dict(observable_part)
    attributes.append({'type': 'email-src', 'object_relation': 'from',
                       'value': addresses[message.pop('from_ref')]})
    for ref in ('to_refs', 'cc_refs', 'ouioui'):
        if ref in message:
            for item in message.pop(ref):
                mapping = email_mapping[ref]
                attributes.append({'type': mapping['type'], 'object_relation': mapping['relation'],
                                   'value': addresses[item]})
    if 'body_multipart' in message:
        for f in message.pop('body_multipart'):
            attributes.append({'type': 'email-attachment', 'object_relation': 'attachment',
                               'value': files[f.get('body_raw_ref')]})
    for m in message:
        if m == 'additional_header_fields':
            fields = message[m]
            for field in fields:
                mapping = email_mapping[field]
                if field == 'Reply-To':
                    for rt in fields[field]:
                        attributes.append({'type': mapping['type'],
                                           'object_relation': mapping['relation'],
                                           'value': rt})
                else:
                    attributes.append({'type': mapping['type'],
                                       'object_relation': mapping['relation'],
                                       'value': fields[field]})
        else:
            try:
                mapping = email_mapping[m]
            except:
                continue
            attributes.append({'type': mapping['type'], 'object_relation': mapping['relation'],
                               'value': message[m]})
    return attributes

def pattern_email(pattern):
    return fill_pattern_attributes(pattern, email_mapping)

def observable_file(observable):
    attributes = []
    observable = dict(observable['0'])
    if 'hashes' in observable:
        hashes = observable.pop('hashes')
        for h in hashes:
            h_type = h.lower().replace('-', '')
            attributes.append({'type': h_type, 'object_relation': h_type,
                               'value': hashes[h]})
    fill_observable_attributes(attributes, observable, file_mapping)
    return attributes

def pattern_file(pattern):
    attributes = []
    for p in pattern:
        p_type, p_value = p.split(' = ')
        if 'file:hashes.' in p:
            _, h = p_type.split('.')
            h = h[1:-1]
            attributes.append({'type': h, 'object_relation': h, 'value': p_value[1:-1]})
        else:
            mapping = file_mapping[p_type]
            attributes.append({'type': mapping['type'], 'object_relation': mapping['relation'],
                               'value': p_value[1:-1]})
    return attributes

def observable_ip_port(observable):
    attributes = []
    if len(observable) >= 2:
        attributes.append({'type': 'ip-dst', 'object_relation': 'ip',
                           'value': observable['0'].get('value')})
        observable_part = dict(observable['1'])
        fill_observable_attributes(attributes, observable_part, ip_port_mapping)
        try:
            observable_part = dict(observable['2'])
        except:
            return attributes
    else:
        observable_part = dict(observable['0'])
    fill_observable_attributes(attributes, observable_part, ip_port_mapping)
    return attributes

def pattern_ip_port(pattern):
    return fill_pattern_attributes(pattern, ip_port_mapping)

def observable_regkey(observable):
    attributes = []
    observable = dict(observable['0'])
    if 'values' in observable:
        values = observable.pop('values')
        fill_observable_attributes(attributes, values[0], regkey_mapping)
    # here following, we don't use the function just used on values bacause we may want to rearrange
    # the strings (such as for regkeys) but not for all the values in all the other objects
    for o in observable:
        try:
            mapping = regkey_mapping[o]
        except:
            continue
        attributes.append({'type': mapping.get('type'), 'object_relation': mapping.get('relation'),
                            'value': observable.get(o).replace('\\\\', '\\')})
    return attributes

def pattern_regkey(pattern):
    attributes = []
    for p in pattern:
        p_type, p_value = p.split(' = ')
        try:
            mapping = regkey_mapping[p_type]
        except KeyError:
            continue
        attributes.append({'type': mapping['type'], 'object_relation': mapping['relation'],
                           'value': p_value.replace('\\\\', '\\')[1:-1]})
    return attributes

def observable_url(observable):
    attributes = []
    for o in observable:
        observable_part = observable[o]
        part_type = observable_part._type
        try:
            mapping = url_mapping[part_type]
        except:
            continue
        try:
            value = observable_part['value']
        except:
            value = observable_part['dst_port']
        attributes.append({'type': mapping['type'], 'object_relation': mapping['relation'],
                           'value': value})
    return attributes

def pattern_url(pattern):
    return fill_pattern_attributes(pattern, url_mapping)

def observable_x509(observable):
    attributes = []
    observable = dict(observable['0'])
    if 'hashes' in observable:
        hashes = observable.pop('hashes')
        fill_observable_attributes(attributes, hashes, x509_mapping)
    fill_observable_attributes(attributes, observable, x509_mapping)
    return attributes

def pattern_x509(pattern):
    return fill_pattern_attributes(pattern, x509_mapping)

objects_mapping = {'domain-ip':{'observable': observable_domain_ip, 'pattern': pattern_domain_ip},
                   'email': {'observable': observable_email, 'pattern': pattern_email},
                   'file': {'observable': observable_file, 'pattern': pattern_file},
                   'ip-port': {'observable': observable_ip_port, 'pattern': pattern_ip_port},
                   'registry-key': {'observable': observable_regkey, 'pattern': pattern_regkey},
                   'url': {'observable': observable_url, 'pattern': pattern_url},
                   'x509': {'observable': observable_x509, 'pattern': pattern_x509}}

domain_pattern_mapping = {'value': {'type': 'domain'}}
ip_pattern_mapping = {'value': {'type': 'ip-dst'}}

external_pattern_mapping = {'domain-name': domain_pattern_mapping,
                            'file': file_mapping,
                            'ipv4-addr': ip_pattern_mapping,
                            'ipv6-addr': ip_pattern_mapping,
                            'x509-certificate': x509_mapping
                            }
