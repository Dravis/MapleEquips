import cv2
import numpy as np
import os
import math

class EquipTemplateMatcher:
    verbose = True
    outputFiles = True
    outputType = 2 #0 = greyscale; 1 = threshold; 2 = template matched
    templates = []
    totalStats = []
    itemsLines = []
    
    def load_templates(self):
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'Star.png'), "*"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'Rare.png'), "Rare Item"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'Epic.png'), "Epic Item"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'Unique.png'), "Unique Item"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'Legendary.png'), "Legendary Item"))

        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'STR.png'), "STR:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'DEX.png'), "DEX:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'INT.png'), "INT:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'LUK.png'), "LUK:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'AttackPower.png'), "Attack Power:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'MagicAttack.png'), "Magic Attack:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'RemainingEnchantments.png'), "Remaining Enchantments:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'MATTper.png'), "M. ATT per "))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'ATT.png'), "ATT:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'BossDamage.png'), "Boss Damage:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'BossDamage_2.png'), "Boss Damage:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'Damage.png'), "Damage:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'IgnoredDEF.png'), "Ignored DEF:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'DEF.png'), "DEF:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'AllStats.png'), "All Stats:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'Speed.png'), "Speed:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'MaxHP.png'), "Max HP:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'MaxHP_2.png'), "Max HP:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'MaxMP.png'), "Max MP:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'MaxMP_2.png'), "Max MP:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'defense.png'), "Defense:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'Jump.png'), "Jump:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'AvailRecoveries.png'), "Available Recoveries:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'HammerApplied.png'), "Hammer Applied:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'CriticalRate.png'), "Critical Rate:"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'CharacterLevels.png'), " Character Levels:"))

        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', '0.png'), "0"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', '0_2.png'), "0"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', '1.png'), "1"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', '1_2.png'), "1"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', '2.png'), "2"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', '3.png'), "3"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', '4.png'), "4"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', '5.png'), "5"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', '6.png'), "6"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', '6_2.png'), "6"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', '7.png'), "7"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', '8.png'), "8"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', '9.png'), "9"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', '9_2.png'), "9"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'leftParenthesis.png'), "("))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'leftParenthesis_2.png'), "("))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'rightParenthesis.png'), ")"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'plus.png'), "+"))
        self.templates.append(self.get_template(os.path.join(os.getcwd(), 'template', 'percent.png'), "%"))
        
    #rezie image
    def resize(self, image, percent):   
        width = int(image.shape[1] * percent / 100)
        height = int(image.shape[0] * percent / 100)
        return cv2.resize(image, (width, height))

    # get grayscale image
    def get_grayscale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     
    #thresholding
    def thresholding(self, image, thresh):
        return cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]

    #template matching
    def match_template(self, image, template):
        return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    #Show an image
    def show_image(self, image):
        cv2.imshow('image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #calculate if pt is near with a certain dist of already matched points or is within a detected zone
    def close_to_other_match(self, matchPtList, pt, dist):
        for mpt in matchPtList:
            #Check if the detected point is near another one
            if math.sqrt(pow(abs(mpt[0][0] - pt[0]), 2) + pow(abs(mpt[0][1] - pt[1]), 2)) < dist:       
                return True
            #Detect if the point is within another detected square
            if (pt[0] >= mpt[0][0] and pt[1] >= mpt[0][1] and pt[0] < (mpt[0][0] + mpt[2][0]) and pt[1] < (mpt[0][1] + mpt[2][1])):
                return True           
        return False

    def match_template_rect(self, baseImg, outImg, template, text, allMatches):
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(baseImg,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        hit=0
        for pt in zip(*loc[::-1]):
            if not self.close_to_other_match(allMatches, pt, 5):
                cv2.rectangle(outImg, pt, (pt[0] + w, pt[1] + h), (255,255,0), 2)
                hit+=1
                allMatches.append([pt, text, [w, h]])
        return allMatches
        
    def get_lines(self, allMatches):   
        lastY = 0
        correctedMatches = []
        
        lists = sorted(allMatches, key=lambda e: e[0][1])
        #Correct Y so that all detected templates on same line will have the same Y coord.
        for li in lists:
            if li[0][1] > lastY + 20:
                lastY = li[0][1]
                correctedMatches.append([[li[0][0], li[0][1]], li[1], [li[2][0], li[2][1]]])
            else:
                correctedMatches.append([[li[0][0], lastY], li[1], [li[2][0], li[2][1]]])   
        
        sortCorrectedMatches = sorted(correctedMatches, key=lambda e: (e[0][1], e[0][0]))
        lines = []
        currentLine = ""
        lastY = 0
        for li in sortCorrectedMatches:
            if li[0][1] > lastY:
                if currentLine != "":
                    lines.append(currentLine)
                currentLine= li[1]
                lastY = li[0][1]
            else:
                currentLine += li[1]
                    
        lines.append(currentLine)
        return lines                    
           
    def get_template(self, pathToImage, text):
        template = cv2.imread(pathToImage)
        template = self.get_grayscale(template)
        return [template, text]

    def template_match_image(self, imgPath):
        if self.verbose:
            print("Template matching file: {}".format(os.path.split(imgPath)[1]))
        img = cv2.imread(imgPath)
        
        img = self.resize(img, 400)
        imgGray = self.get_grayscale(img)
        imgThres = self.thresholding(imgGray, 75)
        
        allMatches = []
        lines = []
        imgTemp = imgThres.copy()
        for tem in self.templates:
            allMatches = self.match_template_rect(imgThres, imgTemp, tem[0], tem[1], allMatches)
        lines = self.get_lines(allMatches)
        
        if self.outputFiles:
            if self.outputType == 0:
                cv2.imwrite(os.path.join(os.getcwd(), 'output', os.path.split(imgPath)[1]), imgGray)
            if self.outputType == 1:
                cv2.imwrite(os.path.join(os.getcwd(), 'output', os.path.split(imgPath)[1]), imgThres)
            if self.outputType == 2:
                cv2.imwrite(os.path.join(os.getcwd(), 'output', os.path.split(imgPath)[1]), imgTemp)
        
        return lines
        
    def get_total_stats(self):
        totals = []
        for item in self.itemsLines:
            stars = 0
            for line in item:
                stat = ""
                total = 0
                base = 0
                bonus1 = 0
                bonus2 = 0          
                
                colonSep = line.find(":")
                if colonSep != -1 and len(line) != colonSep+1:
                    stat = line[0:colonSep]
                    if "%" in line:
                        stat+="%"
                    if line[0] == '(' or line[0] == '+':
                        stat = stat[1:]
                        
                    leftParenthesisSep = line.find("(", colonSep)
                    if leftParenthesisSep == -1:                      
                        totalStr = ''.join(x for x in line[colonSep+1:] if x.isdigit())
                        total = int(totalStr)
                    else:
                        totalStr = ''.join(x for x in line[colonSep+1:leftParenthesisSep] if x.isdigit())
                        total = int(totalStr)
                        
                        values = line[leftParenthesisSep+1:].split("+")
                        if len(values) >= 2:
                            baseStr = ''.join(x for x in values[0] if x.isdigit())
                            base = int(baseStr)
                            
                            bonus1Str = ''.join(x for x in values[1] if x.isdigit())
                            bonus1 = int(bonus1Str)
                        if len(values) == 3:
                            bonus2Str = ''.join(x for x in values[2] if x.isdigit())
                            bonus2 = int(bonus2Str)
                    
                    statFound = False
                    if total != 0 and base == 0 and bonus1 == 0 and bonus2 == 0:
                        base = total
                        
                    for l in totals:
                        if l["stat"] == stat:
                            statFound = True
                            l["total"] += total
                            l["base"] += base
                            l["bonus1"] += bonus1
                            l["bonus2"] += bonus2
                            
                    if statFound == False:
                        totals.append({"stat":stat, "total": total, "base":base, "bonus1":bonus1, "bonus2":bonus2})        
        return totals
        
    def run(self):
        self.load_templates()
        
        if self.verbose:
            print("{} Templates loaded".format(len(self.templates)))
        
        filelist= [file for file in os.listdir('input') if file.endswith('.png')]
        
        if self.verbose:
            print("{} Items loaded".format(len(filelist)))
        
        for file in filelist:
            self.itemsLines.append(self.template_match_image(os.path.join(os.getcwd(), 'input', file)))
            
        self.totalStats = self.get_total_stats()
