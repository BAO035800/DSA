function twoSum(nums: number[], target: number): number[] {
    const numMap = new Map<number, number>(); 

    for (let i = 0; i < nums.length; i++) {
        const currentNum = nums[i];
        const complement = target - currentNum; // Số cần tìm để đạt target

        // 1. KIỂM TRA: Nếu số còn thiếu (complement) đã có trong Map, 
        // nghĩa là ta đã tìm thấy cặp số.
        if (numMap.has(complement)) {
            // Lấy chỉ mục của số complement đã lưu
            const complementIndex = numMap.get(complement)!; 
            
            // Trả về chỉ mục của complement và chỉ mục hiện tại (i)
            return [complementIndex, i];
        }

        // 2. LƯU TRỮ: Nếu chưa tìm thấy, lưu số hiện tại và chỉ mục của nó vào Map
        // để sử dụng trong các lần lặp tiếp theo.
        numMap.set(currentNum, i);
    }

    // Nếu không tìm thấy cặp nào
    return [];
};