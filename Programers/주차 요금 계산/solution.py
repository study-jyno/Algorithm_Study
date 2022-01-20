def solution(fees, records):
    answer = []
    record_dict = {}
    for record in records:
        record_split = record.split(' ')
        if record_split[1] not in record_dict:
            record_dict[record_split[1]] = {}
        record_dict[record_split[1]][record_split[2]] = record_split[0]

    def cal_bill(in_time, out_time, fee):
        total_hour = int(out_time.split(':')[0]) - int(in_time.split(':')[0])
        total_min = int(out_time.split(':')[1]) - int(in_time.split(':')[1])
        total_time = total_hour * 60 + total_min

        if total_time < 0:
            return cal_bill(in_time, '23:59', fee)

        if total_time <= fee[0]:
            return fee[1]
        extra_time = (total_time - fee[0]) // fee[2]
        if (total_time - fee[0]) % fee[2] != 0:
            extra_time += 1
        return fee[1] + extra_time * fee[3]
        # 5000 + ⌈(334 - 180) / 10⌉ x 600

    result = []
    for record in record_dict:
        out_time = "23:59"
        if 'OUT' in record_dict[record]:
            out_time = record_dict[record]['OUT']
        bill = cal_bill(record_dict[record]['IN'], out_time, fees)
        result.append([record, bill])
    return answer


if __name__ == "__main__":
    fees_list = [[180, 5000, 10, 600], [120, 0, 60, 591], [1, 461, 1, 10]]
    records_list = [
        ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
         "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"],
        ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"],
        ["00:00 1234 IN"]]
    result_list = [[14600, 34400, 5000], [0, 591], [14841]]
    for fees, records, result in zip(fees_list, records_list, result_list):
        answer_ = solution(fees, records)
        print(f'answer : {answer_} | result {result}')
